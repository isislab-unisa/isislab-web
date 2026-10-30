(() => {
  'use strict';
  // Only explicit user choices are stored. Browser locale is the first-visit default.
  document.querySelectorAll('[data-language-choice]').forEach(a => {
    a.addEventListener('click', () => {
      try { localStorage.setItem('isislab-language', a.dataset.languageChoice); } catch (e) {}
    });
  });
  const english = document.documentElement.lang === 'en';
  const menu = document.getElementById('main-navigation');
  const trigger = document.querySelector('.nav-toggle');
  const parents = [...document.querySelectorAll('.nav-item--parent')];
  if (trigger && menu) {
    trigger.addEventListener('click', () => {
      const isOpen = menu.classList.toggle('is-active');
      trigger.setAttribute('aria-expanded', String(isOpen));
      trigger.setAttribute('aria-label', isOpen ? (english ? 'Close menu' : 'Chiudi il menu') : (english ? 'Open menu' : 'Apri il menu'));
    });
    menu.addEventListener('click', event => {
      if (event.target.closest('a') && innerWidth <= 920) {
        menu.classList.remove('is-active');
        trigger.setAttribute('aria-expanded', 'false');
      }
    });
  }
  for (const parent of parents) {
    const button = parent.querySelector('.submenu-toggle');
    if (!button) continue;
    button.addEventListener('click', () => {
      const shouldOpen = !parent.classList.contains('is-open');
      for (const other of parents) {
        other.classList.remove('is-open');
        other.querySelector('.submenu-toggle')?.setAttribute('aria-expanded', 'false');
      }
      parent.classList.toggle('is-open', shouldOpen);
      button.setAttribute('aria-expanded', String(shouldOpen));
    });
  }
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      menu?.classList.remove('is-active');
      trigger?.setAttribute('aria-expanded', 'false');
      for (const parent of parents) {
        parent.classList.remove('is-open');
        parent.querySelector('.submenu-toggle')?.setAttribute('aria-expanded', 'false');
      }
    }
  });
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) { entry.target.classList.add('is-visible'); observer.unobserve(entry.target); }
      });
    }, { threshold: 0.08 });
    document.querySelectorAll('.lab-reveal').forEach(el => observer.observe(el));
  } else {document.querySelectorAll('.lab-reveal').forEach(el => el.classList.add('is-visible'));}
})();
