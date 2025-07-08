document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.getElementById('text-input');
    
    textarea.addEventListener('input', function(e) {
        const resultCard = document.getElementById('result');
        if (resultCard) {
            resultCard.classList.add('hidden');
        }
    });
});