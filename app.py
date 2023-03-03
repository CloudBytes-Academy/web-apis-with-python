from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.route("/greet")
def index():
    
    return "Hello world"