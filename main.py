import json
from flask import Flask, request, jsonify

import gpt4free
from gpt4free import Provider

app = Flask(__name__)
@app.route('/')
def chatapi():
    query = "write easy for school"
    response = gpt4free.Completion.create(Provider.You, prompt='Write a poem on Lionel Messi')

    return response
if __name__ == '__main__':
    app.run(debug=True)



