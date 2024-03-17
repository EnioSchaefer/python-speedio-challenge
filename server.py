from flask import Flask, jsonify
from models.connection_options.connection import DBConnectionHandler

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return jsonify({"status": "working"})

if __name__ == '__main__':
    app.run(debug=True)