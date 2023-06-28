import json
from flask import Flask, request, jsonify

from gpt4free import you

app = Flask(__name__)
@app.route('/')
def chatapi():
    query = "write easy for school"
       # simple request with links and details
    response = you.Completion.create(
        prompt="write hashtages for seo",
        detailed=True,
        include_links=True, )

    return response
if __name__ == '__main__':
    app.run(debug=True)



