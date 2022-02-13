from flask import Flask, request, send_file, jsonify
from bin.filters import apply_filter

app = Flask(__name__)

# Read the PIL document to find out which filters are available out-of the box
filters_available = ["blur", "contour", "detail" , "edge_enhance" , "edge_enhance_more" , "emboss" , "find_edges" , "sharpen" , "smooth" , "smooth_more" , ]


@app.route("/", methods=["GET", "POST"])
def index():
    response = {
        "filters_available" : filters_available,
        "usage" : { "http_method" : "POST" , "URL" : "/<filter_available>/" },
    }
    return jsonify(response)


@app.post("/<filter>")
def image_filter(filter):
    if filter not in filters_available:
        response = { "error" : "incorrect filter" } 
        return jsonify(response)
    file = request.files[ "image" ] 
    if not file:
        response = { "error" : "no file provided" } 
        return jsonify(response)
    filtered_image = apply_filter(file, filter)
    return send_file(filtered_image, mimetype= "image/JPEG" )


if __name__ == "__main__":
    app.run()
    