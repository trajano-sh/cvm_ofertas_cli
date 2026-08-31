document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('menuToggle');
  var links = document.getElementById('navLinks');

  toggle.addEventListener('click', function () {
    links.classList.toggle('open');
  });

  links.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () {
      links.classList.remove('open');
    });
  });

  document.querySelectorAll('.copy-btn').forEach(function (btn) {
    var label = btn.querySelector('.copy-label');
    var defaultLabel = label ? label.textContent : '';

    btn.addEventListener('click', function () {
      var code = btn.closest('.code-window').querySelector('pre code');
      if (!code) return;

      navigator.clipboard.writeText(code.textContent).then(function () {
        btn.classList.add('copied');
        if (label) label.textContent = 'Copiado!';

        setTimeout(function () {
          btn.classList.remove('copied');
          if (label) label.textContent = defaultLabel;
        }, 1800);
      });
    });
  });
});
