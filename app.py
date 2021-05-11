from flask import Flask, jsonify, render_template, request
from data import quotes

app = Flask(__name__)

# Home Page


@app.route('/')
def home():
    return render_template('home.html')

# Docs Page


@app.route('/docs')
def docs():
    return render_template('docs.html')

# All Quotes Pages


@app.route('/api/v1/res/all', methods=['GET'])
def api_all():
    return jsonify(quotes)

# Api with ID


@app.route('/api/v1/res/quotes', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        # make a 404 page not found page
        return "[ERROR] No ID field provided.... Please Specify an ID"

    results = []

    for quote in quotes:
        if quote['id'] == id:
            results.append(quote)

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
