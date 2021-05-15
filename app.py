from flask import Flask, jsonify, render_template, request, current_app
import json

app = Flask(__name__)

with open('data.json') as file:
    data = json.load(file)

# Home Page


@app.route('/')
def home():
    return render_template('home.html')

# 404 Page


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404page.html')

# Docs Page


@app.route('/docs')
def docs():
    return render_template('docs.html')

# All Quotes Pages


@app.route('/api/v1/res/all', methods=['GET'])
def api_all():
    return current_app.response_class(json.dumps(data), mimetype="application/json")

# Api with ID


@app.route('/api/v1/res', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        # make a 404 page not found page
        return render_template('404page.html')

    results = []

    for i in data['quotes']:
        if i['id'] == id:
            results.append(i)

    return jsonify(results)


@app.route('/api/v1/res', methods=['GET'])
def api_author():
    if 'author' in request.args:
        author = str(request.args['author'])
    else:
        return render_template('404page.html')

    results = []

    for i in data['quotes']:
        if i['author'] == author:
            results.extend(i)

    return jsonify(results, indents=2)


if __name__ == "__main__":
    app.run(debug=True)
