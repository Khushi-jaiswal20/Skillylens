// Global utilities
document.addEventListener('DOMContentLoaded', () => {
  // Highlight active nav link
  const links = document.querySelectorAll('.nav-links a');
  links.forEach(link => {
    if (link.href === window.location.href) {
      link.style.color = 'var(--text)';
    }
  });
});