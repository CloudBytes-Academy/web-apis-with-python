from flask import Flask, jsonify, request

app = Flask(__name__)

ERROR_MESSAGE = {"status": "error"}


@app.get("/greet")
def index():

    firstname, lastname = request.args.get("firstname"), request.args.get("lastname")

    if firstname and (not lastname):
        response = {"data": f"Hello, {firstname}!"}
    elif (not firstname) and lastname:
        response = {"data": f"Hello, Mr. or Ms. {lastname}!"}
    elif firstname and lastname:
        response = {"data": f"Is your name {firstname} {lastname}?"}
    else:
        return jsonify(ERROR_MESSAGE)

    return jsonify(response)
