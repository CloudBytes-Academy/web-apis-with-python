from typing import List, Optional
from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder


app = FastAPI()

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


@app.api_route("/", methods=["GET", "POST"])
def index():
    """
    Return the usage instructions that specifies
    1. which filters are available, and
    2. the method format
    """
    response = {
        "filters_available": filters_available,
        "usage": {"http_method": "POST", "URL": "/<filter_available>/"},
    }
    return jsonable_encoder(response)
