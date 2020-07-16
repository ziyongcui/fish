from flask import Flask, request, render_template, session, jsonify, redirect, url_for

app = Flask(__name__)

@app.route("/")
def serve_index():
    return render_template("index.html")

@app.route("/createGame")
def createGame():
    return

@app.route("/joinGame")
def createGame():
    return

@app.route("/startGame")
def createGame():
    return


# TODO: not really this
@app.route("/game")
def serve_game():
    return render_template("game.html")

if __name__ == "__main__":
    app.run(debug=True)

