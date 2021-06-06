from typing import List, Optional
from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder
from model.dbHandler import match_exact, match_like

app = FastAPI()


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {"usage": "/dict?=<word>"}
    return jsonable_encoder(response)


@app.get("/dict")
def dictionary(words: List[str] = Query(None)):
    """
    DICTIONARY ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    if not words:
        response = {"status": "error", "word": words, "data": "word not found"}
        return jsonable_encoder(response)

    # Initialise the reponse
    response = {"words": []}

    for word in words:
        # Try to find an exact match
        definitions = match_exact(word)
        if definitions:
            response["words"].append({"status": "success", "word": word, "data": definitions})
        else:
            # Try to find an approximate match
            definitions = match_like(word)
            if definitions:
                response["words"].append({"status": "partial", "word": word, "data": definitions})
            else:
                response[words].append({"status": "error", "word": word, "data": "word not found"})

    return jsonable_encoder(response)
