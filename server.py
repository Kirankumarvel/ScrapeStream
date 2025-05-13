from flask import Flask, jsonify, send_from_directory, request
import os
import json
import logging

app = Flask(__name__)
DATA_FILE = 'scraped_data.json'

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    return "Scraper Server is Running"

@app.route('/data', methods=['GET'])
def get_data():
    app.logger.info("Data route accessed")
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
            app.logger.info("Data successfully retrieved from file")
            return jsonify(data)
        except json.JSONDecodeError as e:
            app.logger.error(f"JSON decode error: {e}")
            return jsonify({'error': 'Data file is not a valid JSON'}), 500
        except Exception as e:
            app.logger.error(f"Unexpected error: {e}")
            return jsonify({'error': 'An unexpected error occurred'}), 500
    else:
        app.logger.warning("Data file not found")
        return jsonify({'error': 'Data file not found'}), 404

@app.route('/favicon.ico')
def favicon():
    app.logger.info("Favicon route accessed")
    try:
        return send_from_directory(os.path.join(app.root_path, ''), 'favicon.ico')
    except FileNotFoundError:
        app.logger.warning("Favicon not found")
        return jsonify({'error': 'Favicon not found'}), 404

@app.errorhandler(404)
def not_found_error(error):
    app.logger.warning(f"404 error: {request.path} not found")
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"500 error: {error}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.logger.info("Starting the Flask server")
    app.run(host='0.0.0.0', port=5000)
