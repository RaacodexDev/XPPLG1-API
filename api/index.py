from flask import Flask, jsonify
import requests

app = Flask(__name__)

JSON_URL = "https://raw.githubusercontent.com/RaacodexDev/XPPLG1/main/pengumuman.json"


@app.route("/papan-pengumuman")
def papan_pengumuman():
    response = requests.get(JSON_URL)

    if response.status_code != 200:
        return jsonify({
            "error": "Gagal mengambil data pengumuman"
        }), 500

    return jsonify(response.json())


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "API XPPLG1 aktif"
    })
