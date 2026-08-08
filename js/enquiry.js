// Course enquiry form — static site, no backend.
// Submits to FormSubmit's AJAX endpoint; falls back to a normal POST if fetch fails.
(function () {
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  var form = document.getElementById('enquiryForm') || document.getElementById('leadForm');
  if (!form) return;
  var isLead = form.id === 'leadForm';

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }

    var btn = form.querySelector('button[type="submit"]');
    var msg = document.getElementById(isLead ? 'leadOk' : 'okMsg');
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
      msg.innerHTML = isLead
        ? '<b>Thank you, ' + (data.get('name') || '') + '.</b> Your checklist is on its way to ' +
          (data.get('email') || 'your inbox') + '. Check your spam folder if it has not arrived in a few minutes.'
        : '<b>Thank you, ' + (data.get('name') || '') + '.</b> Your enquiry about <b>' +
          (data.get('course') || 'our courses') + '</b> has been sent. We will reply to ' +
          (data.get('email') || 'you') + ' within 1–2 working days.';
      msg.classList.add('show');
      msg.scrollIntoView({ behavior: 'smooth', block: 'center' });
      form.reset();
    }).catch(function () {
      // Network/CORS problem — fall back to a plain form POST (FormSubmit thank-you page).
      form.submit();
    }).finally(function () {
      btn.disabled = false;
      btn.textContent = isLead ? 'Send me the checklist' : 'Send enquiry';
    });
  });
})();
