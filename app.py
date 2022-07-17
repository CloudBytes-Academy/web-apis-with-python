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
    # Since this is a website with front-end, we don't need to send the usage instructions
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
    if not word:
        return jsonify({"status": "error", "data": "No a valid word or no word provided."})
    definition = match_exact(word)
    if definition:
        return jsonify({"status": "success", "data": definition})

    definition = match_like(word)
    if definition:
        return jsonify({"status": "partial", "data": definition})

    return jsonify({"status": "error", "data": "word not found"})

if __name__ == "__main__":
    app.run()
