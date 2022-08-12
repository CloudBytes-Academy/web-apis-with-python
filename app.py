from flask import Flask, request, send_file, jsonify
from bin.filters import apply_filter

app = Flask(__name__)

# Read the PIL document to find out which filters are available out-of the box
filters_available = [
 "blur" ,
 "contour" ,
 "detail" ,
 "edge_enhance" ,
 "edge_enhance_more" ,
 "emboss" ,
 "find_edges" ,
 "sharpen" ,
 "smooth" ,
 "smooth_more",]


@app.route("/", methods=["GET", "POST"])
def index():
    """
    TODO:
    1. Return the usage instructions that specifies which filters are available, and the method format
    """
    response = {
                "filters_available" : filters_available,
                "usage" : { "http_method" : "POST" , "URL" : "/<filter_available>/" },
               }
    return jsonify(response)


@app.post("/<filter>")
def image_filter(filter):
    print(f"filter is {filter}")
    print( filter not in filters_available)
    if filter not in filters_available:
        print("0000")
        return jsonify({"status":"error here no filter you want"})
    print("1")
    file = request.files["image"]
    if not file:
        return jsonify({"status":"error missing file"})
    print("2")
    filtered_image = apply_filter(file,filter)
    print("3")
    return send_file(filtered_image,mimetype="image/JPEG")

    """
    TODO:
    1. Checks if the provided filter is available, if not, return an error
    2. Check if a file has been provided in the POST request, if not return an error
    3. Apply the filter using apply_filter() method from bin.filters
    4. Return the filtered image as response
    """
    
if __name__ == "__main__":
    app.run()
    