from flask import Flask, request, jsonify
from ai_model_generator import generate_model

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():

    data = request.json
    prompt = data["prompt"]

    file = generate_model(prompt)

    return jsonify({"file": file})

app.run(port=5000)
