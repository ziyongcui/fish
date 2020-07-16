from flask import Flask, requests, render_template, session

app = Flask(__name__)

@app.route("/")
def serve_index():
    return render_template("index.html")


# TODO: not really this
@app.route("/game")
def serve_index():
    return render_template("game.html")


