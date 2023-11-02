from flask import Flask, request, render_template, redirect

app = Flask(__name__)

ERROR_MESSAGE = {"status": "error"}
GOOGLE_API_ENDPOINT = "https://google.com/search"

@app.get("/")
def index():

    return render_template("index.html")

@app.get("/search")
def search():
    query = request.args.get("q")
    return redirect(f"{GOOGLE_API_ENDPOINT}?q={query}")

if __name__ == "__main__":

    app.run()
