from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    """
    TODO: Render the home page provided under templates/index.html in the repository
    """
    return render_template("index.html")

@app.get("/search")
def search():
    """
    TODO:
    1. Capture the word that is being searched
    2. Seach for the word on Google and display results
    """
    args = request.args.get("q")

    return redirect(f"https://google.com/search?q={args}")


if __name__ == "__main__":
    app.run()