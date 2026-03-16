from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate_model():
    # Logic for model generation
    return jsonify({'message': 'Model generated'}), 200

@app.route('/upload', methods=['POST'])
def upload_model():
    # Logic for file upload
    return jsonify({'message': 'File uploaded'}), 200

@app.route('/download/<model_id>', methods=['GET'])
def download_model(model_id):
    # Logic for file download
    return jsonify({'message': 'File downloaded'}), 200

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_model():
    if 'file' not in request.files:
        return {'error': 'No file part'}, 400
    file = request.files['file']
    if file.filename == '':
        return {'error': 'No selected file'}, 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return {'message': 'File uploaded successfully'}, 201

@app.route('/download/<filename>', methods=['GET'])
def download_model(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

@app.route('/generate', methods=['POST'])
def generate_model():
    # Placeholder for model generation logic
    return {'message': 'Model generated successfully'}, 200

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate_model():
    # Code to generate a 3D model
    model_data = request.json.get('model_data')
    # Logic for model generation
    return jsonify({'message': 'Model generated successfully!', 'model_data': model_data})

@app.route('/upload', methods=['POST'])
def upload_model():
    # Code to upload a 3D model
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    file.save(os.path.join('uploads', file.filename))
    return jsonify({'message': 'Model uploaded successfully!'}), 201

@app.route('/download/<model_name>', methods=['GET'])
def download_model(model_name):
    # Code to download a 3D model
    return jsonify({'message': 'Downloading model: ' + model_name})

if __name__ == '__main__':
    app.run(debug=True)
