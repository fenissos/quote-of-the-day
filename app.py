from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Endpoint da JokeAPI para piadas com setup e punchline
JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit"

# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html') 

# Rota para pegar uma nova piada
@app.route('/quote', methods=['GET'])
def get_quote():
    try:
        response = requests.get(JOKE_API_URL)
        response.raise_for_status()  # Verifica erro na requisição

        # Obtendo os dados da resposta
        joke_data = response.json()

        # Verificando a Resposta
        if joke_data["error"]:
            return jsonify({"error": "Erro na API de piadas"}), 500

        # O setup e delivery como uma piada completa
        setup = joke_data.get("setup", "")
        delivery = joke_data.get("delivery", "")
        joke = f"{setup} {delivery}"

        return jsonify({"quote": joke})

    except Exception as e:
        return jsonify({"error": "Não foi possível carregar as piadas."}), 500

if __name__ == '__main__':
    app.run(debug=True)
