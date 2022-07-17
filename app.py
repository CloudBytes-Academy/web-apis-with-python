from flask import Flask, jsonify, request
from flask import render_template


# Intitialise the app
app = Flask(__name__)


def return_message():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    if not fname and not lname:
        return jsonify({"status": "error"})
    elif fname and not lname:
        response = {"data": f"Hello, {fname}!"}
    elif not fname and lname:
        response = {'data': f"Hello, Mr {lname}"}
    else:
        response = {"data": f"Is your name {fname} {lname}?"}
    return response

# Define what the app does
@app.get("/greet")
def index():
    response = return_message()
    return jsonify(response)


@app.get("/hello")
def hello():
    response = return_message()
    return render_template("hello.html", data = response["data"])
