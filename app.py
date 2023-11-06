import json
from flask import Flask, jsonify
from create_monster import generate_monster
from create_hero import generate_hero
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_hello():
    message = { "message" : "Use the GET route /monster to generate a monster, and the GET route /hero to generate a hero!"}
    return jsonify(message), 200

@app.route('/monster', methods=['GET'])
def get_monster():
    monster = generate_monster()
    monster_JSON = json.loads(monster)
    return jsonify(monster_JSON), 200

@app.route('/hero', methods=['GET'])
def get_hero():
    hero = generate_hero()
    hero_JSON = json.loads(hero)
    return jsonify(hero_JSON), 200

if __name__ == '__main__':
    app.run(debug=True)
