from flask import Flask, request, send_file, jsonify
from bin.filters import apply_filter

app = Flask(__name__)

# Read the PIL document to find out which filters are available out-of the box
filters_available = []


@app.route("/", methods=["GET", "POST"])
def index():
    """
    TODO:
    1. Return the usage instructions that specifies which filters are available, and the method format
    """
    pass


@app.post("/<filter>")
def image_filter(filter):
    """
    TODO:
    1. Checks if the provided filter is available, if not, return an error
    2. Check if a file has been provided in the POST request, if not return an error
    3. Apply the filter using apply_filter() method from bin.filters
    4. Return the filtered image as response
    """
    pass


if __name__ == "__main__":
    app.run()
    