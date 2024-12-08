import os
import logging
from collections import defaultdict
from ortools.linear_solver import pywraplp


class Problem:
    def __init__(self, problem_name, bin_capacity, best_known_number_of_bins):
        self.problem_name = problem_name
        self.bin_capacity = bin_capacity
        self.best_known_number_of_bins = best_known_number_of_bins
        self.items = []

    def add_item(self, item_size):
        self.items.append(item_size)

    def display_info(self):
        logging.info("#" * 20)
        logging.info(f"PROBLEM = {self.problem_name}")
        logging.info(f"BIN CAPACITY = {self.bin_capacity}")
        logging.info(f"BEST KNOWN NUMBER OF BINS = {self.best_known_number_of_bins}")
        logging.info(f"# OF ITEMS = {len(self.items)}")
        logging.info(f"ITEMS = {self.items}")
        logging.info("#" * 20 + "\n")


def read_problem_data(fn):
    problems = []
    number_of_problems = None
    file_section = "A"
    with open(fn, "r") as f:
        for line in f:
            if line[0] == "#" or line.strip() == "":
                continue
            if number_of_problems is None:
                number_of_problems = int(line)
                continue
            if file_section == "A":
                problem_name = line.strip()
                file_section = "B"
                continue
            if file_section == "B":
                bin_capacity, number_of_items, best_known_number_of_bins = line.split()
                bin_capacity, number_of_items, best_known_number_of_bins = (
                    int(bin_capacity),
                    int(number_of_items),
                    int(best_known_number_of_bins),
                )
                file_section = "C"
                a_problem = Problem(
                    problem_name, bin_capacity, best_known_number_of_bins
                )
                i = 0
                continue
            if file_section == "C":
                a_problem.add_item(int(line))
                if i < number_of_items - 1:
                    i += 1
                else:
                    problems.append(a_problem)
                    file_section = "A"
    return problems


def solve(a_problem, time_limit=600, max_bins=None):
    # solver_engine = "SCIP"
    # solver_engine = "CPLEX"
    solver_engine = "CBC"
    solver = pywraplp.Solver.CreateSolver(solver_engine)
    if not solver:
        return

    # decision variables
    N = len(a_problem.items)
    if max_bins is not None:
        max_bins = N

    x = {}
    for i in range(N):
        for j in range(max_bins):
            x[(i, j)] = solver.BoolVar(f"x_{i}_{j}")

    # y[j] = 1 if bin j is used.
    y = {}
    for j in range(max_bins):
        y[j] = solver.BoolVar(f"y_{j}")

    # constraints
    # Each item must be in exactly one bin.
    for i in range(N):
        solver.Add(sum(x[i, j] for j in range(max_bins)) == 1)

    # The amount packed in each bin cannot exceed its capacity.
    for j in range(max_bins):
        solver.Add(
            sum(x[(i, j)] * w for i, w in enumerate(a_problem.items))
            <= y[j] * a_problem.bin_capacity
        )
    # objective
    solver.Minimize(solver.Sum([y[j] for j in range(max_bins)]))

    # solve
    logging.info(f"Solving with {solver.SolverVersion()}")
    if solver_engine not in ["CBC"]:
        solver.EnableOutput()
    solver.set_time_limit(time_limit * 1000)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        num_bins = 0
        for j in range(max_bins):
            if y[j].solution_value() == 1:
                bin_items = []
                bin_weight = 0
                for i, w in enumerate(a_problem.items):
                    if x[i, j].solution_value() > 0:
                        bin_items.append(i)
                        bin_weight += w
                if bin_items:
                    num_bins += 1
                    logging.info(
                        f"Bin number = {j}, items packed = {bin_items}, total weight = {bin_weight}"
                    )
        logging.info(f"\nNumber of bins used = {num_bins}")
        logging.info(f"Time = {solver.WallTime()} milliseconds")
        return num_bins
    else:
        logging.info("No feasible solution found.")


def solve_single():
    fn = os.path.join(os.path.dirname(__file__), "instance.txt")
    problems = read_problem_data(fn)
    a_problem = problems[0]
    # num_bins = solve(a_problem, time_limit=30, max_bins=55)
    num_bins = solve(a_problem, time_limit=60)
    logging.info(num_bins)


def solve_all():
    fn = os.path.join(os.path.dirname(__file__), "instance.txt")
    out = ""
    c = 0
    for a_problem in read_problem_data(fn):
        a_problem.display_info()
        num_bins = solve(a_problem, time_limit=60)
        if num_bins == a_problem.best_known_number_of_bins:
            c += 1
        out += f"{a_problem.problem_name}, bins = {num_bins}, optimal bins = {a_problem.best_known_number_of_bins} {"(*)" if num_bins == a_problem.best_known_number_of_bins else ""}\n"
    logging.info(out)
    logging.info(f"Optimality reached in {c} instances")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    # solve_single()
    solve_all()
