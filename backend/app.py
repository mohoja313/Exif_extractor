
import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
from exif_extractor import extract_exif
from database_handler import DatabaseHandler
from bson.objectid import ObjectId # Import ObjectId

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# MongoDB connection
db_handler = DatabaseHandler("mongodb://yourlink/", "database_name", "collection_name")

@app.route('/', methods=['GET'])
def welcome():
    return "use /upload to upload images."
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        exif_data = extract_exif(file_path)
        exif_data["filename"] = filename
        db_handler.insert_data(exif_data)

        # Convert ObjectId to string
        def convert_objectid(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    data[key] = convert_objectid(value)
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    data[i] = convert_objectid(item)
            elif isinstance(data, ObjectId):
                return str(data)
            return data

        exif_data = convert_objectid(exif_data)

        return jsonify(exif_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
