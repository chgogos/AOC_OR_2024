import os
import logging
from collections import defaultdict
from ortools.sat.python import cp_model


class Problem:
    def __init__(self):
        pass

    def display_info(self):
        pass


def read_problem_data(fn):
    a_problem = Problem()
    with open(fn, "r") as f:
        for line in f:
            pass
    return a_problem


def solve(a_problem, time_limit=600):
    model = cp_model.CpModel()

    # decision variables

    # constraints

    # objective

    # solve
    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = time_limit
    status = solver.solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"status: {solver.StatusName(status)}")
        print(f"obj={int(solver.ObjectiveValue()):,}")
        print(f"bound={int(solver.BestObjectiveBound()):,}")
        print(f"time={solver.WallTime():.1f}")

    else:
        print("No solution found.")
        print(f"Status: {solver.StatusName(status)}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    fn = os.path.join(os.path.dirname(__file__), "instance.txt")
    a_problem = read_problem_data(fn)
    a_problem.display_info()
    solve(a_problem)
