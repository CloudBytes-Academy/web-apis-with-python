# dictionary-api-python-flask/app.py
from flask import Flask, request, jsonify, render_template
from model.dbHandler import match_exact, match_like

app = Flask(__name__)


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {"usage": "/dict?=<word>"}
    return jsonify(response)


@app.get("/dict")
def dictionary():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    word = request.args.get("word")

    # Return an error querystring is malformed
    if not word:
        response = {"status": "error", "word": word, "data": "word not found"}
        return jsonify(response)

    # Try to find an exact match
    definitions = match_exact(word)
    if definitions:
        response = {"status": "success", "word": word, "data": definitions}
        return jsonify(response)

    # Try to find an approximate match
    definitions = match_like(word)
    if definitions:
        response = {"status": "partial", "word": word, "data": definitions}
        return jsonify(response)
    else:
        response = {"status": "error", "word": word, "data": "word not found"}
        return jsonify(response)



if __name__ == "__main__":
    app.run()
