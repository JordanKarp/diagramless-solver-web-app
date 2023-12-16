from flask import Flask, request, render_template, session
import os

from solver.main import run

app = Flask(__name__)
app.secret_key = "BAD_SECRET_KEY"


PORT = os.getenv("PORT", default=5000)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/solve", methods=["POST", "GET"])
def solve():
    if request.method == "POST":
        form_data = request.form
        # Retrieve user inputs from the form
        rows = form_data.get("rows")
        columns = form_data.get("columns")
        aClues = form_data.get("acrossClues")
        dClues = form_data.get("downClues")
        sym = form_data.get("sym")
        starting = form_data.get("starting")
        findAll = form_data.get("findAll") == "on"

        solutions = run(rows, columns, aClues, dClues, sym, starting, findAll)

        session["puzzle"] = form_data
        session["solutions"] = solutions
    elif request.method == "GET":
        form_data = session["puzzle"]
        solutions = session["solutions"]

    return render_template("solve.html", puzzle=form_data, solutions=solutions)


@app.route("/print")
def print():
    puzzle = session.get("puzzle", None)
    solutions = session.get("solutions", None)
    sol = solutions[request.form.get("printer", 0)]

    if puzzle and sol:
        return render_template("print.html", puzzle=puzzle, solution=sol)

    return render_template("index.html")
    # return render_template("print.html", puzzle=puzzle, solutions=solutions)


if __name__ == "__main__":
    app.run(port=PORT)
