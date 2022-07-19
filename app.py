from flask import Flask, request, send_file, jsonify
from bin.filters import apply_filter

app = Flask(__name__)

# Read the PIL document to find out which filters are available out-of the box
filters_available = [
    "blur",
    "contour",
    "detail",
    "edge_enhance",
    "edge_enhance_more",
    "emboss",
    "find_edges",
    "sharpen",
    "smooth",
    "smooth_more",
]


@app.route("/", methods=["GET", "POST"])
def index():
    """
    TODO:
    1. Return the usage instructions that
    a) specifies which filters are available
    b) specified the method format
    """
    response = {
        "filters_avaliable": filters_available,
        "usage": {"http_methods": "POST", "URL": "/<filters_available>/"}
    }
    return jsonify(response)

@app.post("/<filter>")
def image_filter(filter):
    """
    TODO:
    1. Checks if the provided filter is available, if not, return an error
    2. Check if a file has been provided in the POST request, if not return an
       error
    3. Apply the filter using apply_filter() method from bin.filters
    4. Return the filtered image as response
    """
    file = request.files["image"]
    if file and filter in filters_available:
        # response = {"status": "file uploaded"}
        filtered_image = apply_filter(file, filter)
        return send_file(filtered_image, mimetype="image/JPEG")
    elif not file:
        response = {"error": "incorrect filter"}
    elif filter not in filters_available:
        response = {"error": "incorrect filter"}
    else:
        response = {"error": "something wrong"}

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
