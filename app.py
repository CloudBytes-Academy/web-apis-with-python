from flask import Flask, jsonify, request, render_template

# Intitialise the app
app = Flask(__name__)

# Define what the app does

"""
#     TODO:
#     1. Capture first name & last name
#     2. If either is not provided: respond with an error
#     3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
#     4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
#     5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
#     """

@app.route("/", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")

        if not name and not surname:
            response = {"status" : "error"}
            return jsonify(response)
        elif name and not surname:
            response = {"data" : f"Hello, {name} !"}
            return jsonify(response)
        elif not name and surname:
            response = {"data" : f"Hello, Mr {surname} !"}
            return jsonify(response)
        else:
            response = {"data" : f"Is yor name {name} {surname} ?"}
            return jsonify(response)
    return render_template("index.html")