from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = [
    { "username": "Woh", "password": "Anything" },
    { "username": "qwiki", "password": "252500" },
    { "username": "electron", "password": "0909" },
    { "username": "Genghis", "password": "Khan" },
    { "username": "Vas", "password": "vasisthebestcoder" }
]

@app.route('/users')
def get_users():
    return jsonify(users)

app.run(host='0.0.0.0', port=8080)
