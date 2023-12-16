from solver.puzzle import Puzzle
from solver.details import PuzzleDetails, SolverDetails
from solver.converter import process_cluestring
from solver.value import SYMMETRIES


def run(rows, columns, acc, down, symmetry, starting, findAll):
    try:
        dimensions = (int(rows), int(columns))
        acrossClueNumbers = [int(x) for x in acc.split(" ")]
        downClueNumbers = [int(x) for x in down.split(" ")]
        cluestring = process_cluestring(acrossClueNumbers, downClueNumbers)
        symmetryFormatted = SYMMETRIES[symmetry]
        startingSquare = int(starting)
        useSymmetry = symmetry not in ["", "Asymmetry"]
        useStarting = startingSquare != 0

        puzzle_details = PuzzleDetails(
            dimensions, cluestring, symmetryFormatted, startingSquare
        )
        solver_details = SolverDetails(
            useSymmetry, useStarting, findAll, True, True, False
        )
        puzzle = Puzzle(puzzle_details, solver_details)
        solutions = puzzle.solve()
        return solutions.return_grids()
    except Exception:
        return []
