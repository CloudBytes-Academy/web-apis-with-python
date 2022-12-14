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
    # args = request.args.get("word")
    # Since this is a website with front-end, we don't need to send the usage instructions
    return render_template("index.html")


@app.get("/dict")
def dictionary():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    words = request.args.getlist("word")

    if not words:
        response = {"status":"error", "word":words, "data":"word not found"}
        return jsonify(response)

    response = {"words":[]}
    
    for word in words:
        definitions = match_exact(word)
        if definitions:
            response["words"].append({"status":"success","word":word,"data":definitions})
        else:
            definitions = match_like(word)
            if definitions:
                response["words"].append({"status":"partial","word":word,"data":definitions})
            else:
                response["words"].append({"status":"error","word":word,"data":"word not found"})

    return render_template("results.html", response=jsonify(response))

if __name__ == "__main__":
    app.run()
