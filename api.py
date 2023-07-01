
import json
from flask import Flask, jsonify
from criar_monstro import gerar_monstro
from criar_heroi import gerar_heroi

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_hello():
    mensagem = { "messagem" : "Use a rota /monstro, para gerar um monstro, e a rota /heroi, para gerar um heroi!"}
    return jsonify(mensagem), 200


@app.route('/monstro', methods=['GET'])
def get_monstro():
    monstro = gerar_monstro()
    monstro_JSON = json.loads(monstro)
    return jsonify(monstro_JSON), 200


@app.route('/heroi', methods=['GET'])
def get_heroi():
    heroi = gerar_heroi()
    heroi_JSON = json.loads(heroi)
    return jsonify(heroi_JSON), 200

if __name__ == '__main__':
    app.run(debug=True)

# IMG HANDLE; 

