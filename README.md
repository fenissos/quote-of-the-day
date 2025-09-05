# Projeto: Quote of the Day

Este é um projeto simples que exibe piadas (ou trocadilhos) no formato de "setup" e "delivery". O backend foi feito com **Flask** e o frontend é simples, utilizando **HTML**, **CSS**, e **JavaScript**. O frontend consome a **JokeAPI** para buscar as piadas.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte maneira:

quote-of-the-day/
│
├── app.py 
├── templates/ 
│ └── index.html 
├── static/ 
│ ├── css/ 
│ │ └── style.css 
│ └── js/
│ └── script.js 
└── requirements.txt 


## Tecnologias Utilizadas

- **Flask**: Para o backend.
- **JokeAPI**: Para fornecer as piadas.
- **HTML/CSS/JS**: Para o frontend.

## Como Rodar o Projeto

### Passo 1: Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/usuario/quote-of-the-day.git
```
cd quote-of-the-day

### Passo 2: Criar um ambiente Virtual

```bash
python3.12 -m venv venv
```

entre no ambiente virtual :D

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Rodar o Backend

```bash
python app.py
```

### Passo 5: Acessar o Frontend

http://127.0.0.1:5000/
