// static/scripts.js
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
        // Remove highlight from all cards
        document.querySelectorAll('.card').forEach(c => c.classList.remove('bg-info'));

        // Add highlight to the clicked card
        card.classList.add('bg-info');
    });
});
