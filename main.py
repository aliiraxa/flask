import json
from flask import Flask, request, jsonify


app = Flask(__name__)
@app.route('/')
def chatapi():
    response="hello"
    return response

