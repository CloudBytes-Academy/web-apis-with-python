from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """
    # Grab variable 'name' from query string
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    if fname and not lname:
        return jsonify({"Hey":f"{fname}!"})
    elif lname and not fname:
        return jsonify({f"Cirle": f"{lname}!"})
    elif lname and fname:
        return jsonify({"They call me": f"{fname} {lname}!"})
    else:
        return jsonify({"I": "am a circle and I identified as a circle"})