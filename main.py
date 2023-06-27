import json
from flask import Flask, request, jsonify


app = Flask(__name__)
@app.route('/')
def chatapi():
    response="hello"
    return response
if __name__ == '__main__':
    app.run(debug=True)
