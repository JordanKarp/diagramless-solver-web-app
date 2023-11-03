from flask import Flask, request, render_template
import os

from solver.main import run

app = Flask(__name__)

PORT = os.getenv("PORT")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/solve", methods=["POST"])
def solve():
    form_data = request.form
    # Retrieve user inputs from the form
    rows = form_data.get("rows")
    columns = form_data.get("columns")
    acrossClues = form_data.get("acrossClues")
    downClues = form_data.get("downClues")
    symmetry = form_data.get("symmetry")
    starting = form_data.get("starting")
    connected = form_data.get("connected") == "on"
    findAll = form_data.get("findAll") == "on"

    solutions = run(
        rows, columns, acrossClues, downClues, symmetry, starting, connected, findAll
    )

    return render_template("solve.html", puzzle=form_data, solutions=solutions)


if __name__ == "__main__":
    app.run(port=PORT)
