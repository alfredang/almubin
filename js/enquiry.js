// Course enquiry form — static site, no backend.
// Submits to FormSubmit's AJAX endpoint; falls back to a normal POST if fetch fails.
(function () {
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  var form = document.getElementById('enquiryForm');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }

    var btn = form.querySelector('button[type="submit"]');
    var msg = document.getElementById('okMsg');
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
      msg.innerHTML = '<b>Thank you, ' + (data.get('name') || '') + '.</b> Your enquiry about <b>' +
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
      btn.textContent = 'Send enquiry';
    });
  });
})();
