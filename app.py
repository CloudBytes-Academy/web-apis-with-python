from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/greet")
def index():
    response = {"data":"value is hellow world"}
    return jsonify(response)