// Função para pegar uma nova piada
function newQuote() {
    fetch('http://127.0.0.1:5000/quote')
        .then(response => response.json())
        .then(data => {
            if (data.quote) {
                const quoteElement = document.getElementById('quote');
                quoteElement.innerText = data.quote;

                const quoteBox = document.querySelector('.quote-box');
                quoteBox.classList.remove('show');  
                setTimeout(() => {
                    quoteBox.classList.add('show');  
                }, 100); 
            } else {
                document.getElementById('quote').innerText = "Não conseguimos encontrar uma piada!";
            }
        })
        .catch(error => {
            document.getElementById('quote').innerText = "Ocorreu um erro! Tente novamente.";
        });
}

window.onload = newQuote;
