document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Animate elements when they come into view
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.card, .project-card, .publication-item, .book-review-card').forEach((el) => {
        observer.observe(el);
    });

    // Add loading animation to images
    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('load', function() {
            this.classList.add('loaded');
        });
    });

    // Add dark mode toggle functionality
    const themeTarget = document.documentElement; // Use <html> for theme attribute
    const darkModeToggle = document.querySelector('[data-md-color-scheme]');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            const currentScheme = themeTarget.getAttribute('data-md-color-scheme') || 'default';
            const newScheme = currentScheme === 'default' ? 'slate' : 'default';
            themeTarget.setAttribute('data-md-color-scheme', newScheme);
            localStorage.setItem('theme', newScheme);
        });
    }

    // Initialize theme from localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        themeTarget.setAttribute('data-md-color-scheme', savedTheme);
    } else {
        // Optionally, set default theme
        themeTarget.setAttribute('data-md-color-scheme', 'default');
    }
});
