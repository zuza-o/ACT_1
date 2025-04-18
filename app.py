from flask import Flask, jsonify

from csv_importer import get_data

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/importer/')
def importer_page():
    data = get_data()
    return jsonify({"message": "imported data: " + str(data)})


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request"}), 400


if __name__ == '__main__':
    app.run()