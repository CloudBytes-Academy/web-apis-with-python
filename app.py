from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.route("/greet")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """
    fname = request.args.get("fname")
    lname = request.args.get("lname")

    if not fname and not lname:
        # If both first name and last name are missing, return an error
        return jsonify({"status": "error"})
    elif fname and not lname:
        # If first name is present but last name is missing
        response = {"data": f"Hello, {fname}!"}
    elif not fname and lname:
        # If first name is missing but last name is present
        response = {"data": f"Hello, Mr. {lname}!"}
    else:
        # if none of the above is true, then both names must be present
        response = {"data": f"Is your name {fname} {lname}?"}

    return jsonify(response)