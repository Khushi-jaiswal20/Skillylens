function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  const icon  = document.getElementById('themeIcon');
  const label = document.getElementById('themeLabel');
  if (!icon || !label) return;
  if (theme === 'light') {
    icon.textContent  = '🌙';
    label.textContent = 'Dark';
  } else {
    icon.textContent  = '☀️';
    label.textContent = 'Light';
  }
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'dark';
  const next    = current === 'light' ? 'dark' : 'light';
  localStorage.setItem('sl-theme', next);
  applyTheme(next);
}

// Apply on every page load
(function () {
  const saved = localStorage.getItem('sl-theme');
  applyTheme(saved || 'dark');
})();