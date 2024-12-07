import os
import logging
from collections import defaultdict
from ortools.sat.python import cp_model


class Problem:
    def __init__(self, number_of_segments, number_of_possibilities):
        self.number_of_segments = number_of_segments
        self.number_of_possibilities = number_of_possibilities
        self.possibilities = []

    def add_possibility(self, cost, segments_combination):
        self.possibilities.append((cost, segments_combination))

    def display_info(self):
        assert self.number_of_possibilities == len(self.possibilities)
        logging.info(f"# segments = {self.number_of_segments}")
        logging.info(f"# possibilities = {self.number_of_possibilities}")
        for i, (cost, possibility) in enumerate(self.possibilities):
            if i >= 20 and i <= self.number_of_possibilities - 20:
                continue
            logging.info(f"Possibility index={i}, cost={cost}, segments={possibility}")


def read_problem_data(fn):
    with open(fn, "r") as f:
        file_section = "A"
        for line in f:
            if line[0] == "#":
                continue
            if line.strip() == "":
                continue
            if file_section == "A":
                number_of_segments, number_of_possibilities = line.split()
                a_problem = Problem(
                    int(number_of_segments), int(number_of_possibilities)
                )
                file_section = "B"
                continue
            if file_section == "B":
                v = line.split()
                a_problem.add_possibility(int(v[0]), [int(x) for x in v[2:]])
    return a_problem


def solve(a_problem, time_limit=600):
    model = cp_model.CpModel()

    # decision variables
    x = {}
    for i in range(a_problem.number_of_possibilities):
        x[i] = model.new_bool_var(f"x_{i}")

    # constraint: each segment must be covered by at least one of the possibilities
    for j in range(a_problem.number_of_segments):
        selected_xs = []
        for i, (_, segments) in enumerate(a_problem.possibilities):
            if j + 1 in segments:
                selected_xs.append(x[i])
        model.add(sum(selected_xs) >= 1)

    # objective
    obj = sum(
        x[i] * a_problem.possibilities[i][0]
        for i in range(a_problem.number_of_possibilities)
    )
    model.minimize(obj)

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = time_limit
    status = solver.solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"status: {solver.StatusName(status)}")
        print(f"obj={int(solver.ObjectiveValue()):,}")
        print(f"bound={int(solver.BestObjectiveBound()):,}")
        print(f"time={solver.WallTime():.1f}")
        for i in range(a_problem.number_of_possibilities):
            if solver.value(x[i]) == 1:
                logging.info(f"Selected possibility {i} : {a_problem.possibilities[i]}")
    else:
        print("No solution found.")
        print(f"Status: {solver.StatusName(status)}")


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    fn = os.path.join(os.path.dirname(__file__), "instance.txt")
    a_problem = read_problem_data(fn)
    a_problem.display_info()
    solve(a_problem, time_limit=600)
