document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle Logic
    const themeToggle = document.getElementById('theme-toggle');
    const docElement = document.documentElement;

    const applyTheme = (theme) => {
        if (theme === 'dark') {
            docElement.classList.add('dark-mode');
        } else {
            docElement.classList.remove('dark-mode');
        }
    };

    const savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);

    themeToggle.addEventListener('click', () => {
        const newTheme = docElement.classList.contains('dark-mode') ? 'light' : 'dark';
        applyTheme(newTheme);
        localStorage.setItem('theme', newTheme);
    });

    // Flash message handler
    document.querySelectorAll('.alert').forEach(alertElement => {
        // Handle OTP pop-up
        if (alertElement.classList.contains('alert-otp-display')) {
            alert(alertElement.textContent.trim());
            alertElement.remove();
        } else {
            // Auto-dismiss other messages
            setTimeout(() => {
                alertElement.style.transition = 'opacity 0.5s ease';
                alertElement.style.opacity = '0';
                setTimeout(() => alertElement.remove(), 500);
            }, 5000);
        }
    });
});