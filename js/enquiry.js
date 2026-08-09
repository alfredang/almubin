// Course enquiry form — static site, no backend.
// Submits to FormSubmit's AJAX endpoint; falls back to a normal POST if fetch fails.
(function () {
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  // WhatsApp widget — toggles the suggested-query panel. Set up before the
  // form guard below, which returns early on pages that have no enquiry form.
  var waToggle = document.getElementById('waToggle');
  var waPanel = document.getElementById('waPanel');
  if (waToggle && waPanel) {
    var setWaOpen = function (open) {
      waPanel.hidden = !open;
      waToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    waToggle.addEventListener('click', function (e) {
      e.stopPropagation();
      setWaOpen(waPanel.hidden);
    });
    var waClose = waPanel.querySelector('.wa-close');
    if (waClose) waClose.addEventListener('click', function () { setWaOpen(false); });
    // Click outside or press Escape to dismiss.
    document.addEventListener('click', function (e) {
      if (!waPanel.hidden && !waPanel.contains(e.target)) setWaOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !waPanel.hidden) { setWaOpen(false); waToggle.focus(); }
    });
  }

  // A page can carry several of these at once — a course page has both the course
  // enquiry form and the contact form — so wire up every one that is present.
  var FORMS = [
    { id: 'enquiryForm', ok: 'okMsg', label: 'Send enquiry' },
    { id: 'leadForm', ok: 'leadOk', label: 'Send me the checklist' },
    { id: 'contactForm', ok: 'contactOk', label: 'Send message' }
  ];

  var successText = function (id, data) {
    var name = data.get('name') || '';
    var email = data.get('email') || 'you';
    if (id === 'leadForm') {
      return '<b>Thank you, ' + name + '.</b> Your checklist is on its way to ' +
        (data.get('email') || 'your inbox') +
        '. Check your spam folder if it has not arrived in a few minutes.';
    }
    if (id === 'contactForm') {
      return '<b>Thank you, ' + name + '.</b> Your message has been sent. ' +
        'We will reply to ' + email + ' within 1–2 working days.';
    }
    return '<b>Thank you, ' + name + '.</b> Your enquiry about <b>' +
      (data.get('course') || 'our courses') + '</b> has been sent. We will reply to ' +
      email + ' within 1–2 working days.';
  };

  FORMS.forEach(function (cfg) {
    var form = document.getElementById(cfg.id);
    if (!form) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }

      var btn = form.querySelector('button[type="submit"]');
      var msg = document.getElementById(cfg.ok);
      var data = new FormData(form);
      var ajaxUrl = form.action.replace('formsubmit.co/', 'formsubmit.co/ajax/');
      btn.disabled = true;
      btn.textContent = 'Sending…';

      fetch(ajaxUrl, {
        method: 'POST',
        body: data,
        headers: { 'Accept': 'application/json' }
      }).then(function (res) {
        if (!res.ok) throw new Error('send failed');
        return res.json();
      }).then(function () {
        msg.innerHTML = successText(cfg.id, data);
        msg.classList.add('show');
        msg.scrollIntoView({ behavior: 'smooth', block: 'center' });
        form.reset();
      }).catch(function () {
        // Network/CORS problem — fall back to a plain form POST (FormSubmit thank-you page).
        form.submit();
      }).finally(function () {
        btn.disabled = false;
        btn.textContent = cfg.label;
      });
    });
  });
})();
