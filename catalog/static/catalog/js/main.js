// Scroll to top button
const scrollBtn = document.getElementById('scrollTop');
if (scrollBtn) {
    window.addEventListener('scroll', () => {
        scrollBtn.style.opacity = window.scrollY > 300 ? '1' : '0';
        scrollBtn.style.pointerEvents = window.scrollY > 300 ? 'auto' : 'none';
    });
    scrollBtn.style.opacity = '0';
    scrollBtn.style.transition = 'opacity 0.3s ease';
}

// Active nav link
const path = window.location.pathname;
document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('href') === path) {
        link.classList.add('active');
    }
});