from flask import Flask, request, jsonify
from gpt4free import you
app = Flask(__name__)
@app.route('/')
def chatapi():
    query = request.args.get('q')
    response = you.Completion.create(
        prompt="hello world",
        detailed=True,
        include_links=True, )
    return response.dict()

if __name__ == '__main__':
    app.run(debug=True)




