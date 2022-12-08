from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/greet")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """
    name = request.args.get("name")
    surname = request.args.get("surname")
    
    if not name and not surname:
        response = {"status" : "error"}
    elif name and not surname:
        response = {"data" : f"Hello, {name} !"}
    elif not name and surname:
        response = {"data" : f"Hello, Mr {surname} !"}
    else:
        response = {"data" : f"Is yor name {name} {surname} ?"}

    return jsonify(response)