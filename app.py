from flask import Flask, request, render_template, redirect
import random

app = Flask(__name__)


@app.get("/")
def index():
    """
    TODO: Render the home page provided under templates/index.html in the repository
    """
    return render_template("index.html")


@app.get("/search")
def search():
   args=request.args.get("q")
   return redirect(f"https://google.com/search?q={args}")

@app.get("/lucky")
def lucky():
    with open("textFile.txt", "r") as file:
        text = file.read()
        words = list(map(str, text.split()))
        arg= random.choice(words)
        return redirect(f"https://google.com/search?q={arg}")
	

if __name__ == "__main__":
    app.run()