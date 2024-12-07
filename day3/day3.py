import os
import logging
from ortools.linear_solver import pywraplp


def main(costs):
    num_workers = len(costs)
    num_tasks = len(costs[0])

    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        return

    # x[i, j] will be 1 if worker i is assigned to task j.
    x = {}
    for i in range(num_workers):
        for j in range(num_tasks):
            x[i, j] = solver.IntVar(0, 1, "")

    # Constraint1: Each worker is assigned to at most 1 task.
    for i in range(num_workers):
        solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) <= 1)

    # Constraint2: Each task is assigned to exactly one worker.
    for j in range(num_tasks):
        solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 1)

    # Objective
    objective_terms = []
    for i in range(num_workers):
        for j in range(num_tasks):
            objective_terms.append(costs[i][j] * x[i, j])
    solver.Minimize(solver.Sum(objective_terms))

    # Solve
    logging.info(f"Solving with {solver.SolverVersion()}")
    solver.EnableOutput()
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        logging.info(f"Total cost = {solver.Objective().Value()}\n")
        for i in range(num_workers):
            for j in range(num_tasks):
                if x[i, j].solution_value() > 0.5: # tolerance for floating point arithmetic
                    logging.info(f"Worker {i} assigned to task {j}." + f" Cost: {costs[i][j]}")
    else:
        logging.info("No solution found.")


def read_data(input_file):
    costs = []
    first_line = True
    k = 0
    cost_line = []
    with open(input_file, "r") as f:
        for line in f:
            if line[0] == "#":
                continue
            if line.strip() == "":
                continue
            if first_line:
                number_of_workers = int(line)
                first_line = False
                continue
            for x in line.split():
                cost_line.append(int(x))
                k += 1
                if k == number_of_workers:
                    costs.append(cost_line)
                    cost_line = []
                    k = 0
    return costs


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    fn = os.path.join(os.path.dirname(__file__), "instance.txt")
    costs = read_data(fn)
    logging.debug(costs)
    main(costs)
