'''
instance: u120_00
--- CP_SAT ---
    49 bins, status: OPTIMAL
    time=1.2
    48 bins, status: OPTIMAL
    time=149.6
    47 bins, No solution found.
    Status: INFEASIBLE, walltime: 0.810061
    --- (with objective)
    status: OPTIMAL
    objective: 48
    walltime: 309.059

--- CBC ---

--- SCIP ---
    49 bins, CIP Status        : problem is solved [optimal solution found]
    Solving Time (sec) : 46.00
    48 bins, SCIP Status        : problem is solved [optimal solution found]
    Solving Time (sec) : 266.00
    47 bins, SCIP Status        : problem is solved [infeasible]
    Solving Time (sec) : 0.00
    --- (with objective)
    SCIP Status        : solving was interrupted [time limit reached]
    Solving Time (sec) : 600.00
    Primal Bound       : +1.00000000000000e+20 (0 solutions)
    Dual Bound         : +4.80000000000000e+01
    Gap                : infinite
    No solution found.
'''
from ortools.sat.python import cp_model
from ortools.linear_solver import pywraplp

class Problem:
    def __init__(self, fn):

        with open(fn, "r") as f:
            lines = f.readlines()

        for i,line in enumerate(lines):
            line = line.strip()
            if i==0:
                self.name = line
                continue
            if i==1:
                items = line.split()
                self.capacity = int(items[0])
                self.num_items = int(items[1])
                self.max_bins = int(items[2])
            break
            # if len(line)==0 or line.startswith("#"):
            #     continue

        self.sizes = []
        for line in lines[i+1:]:
            line = line.strip()
            if len(line)==0:
                continue

            self.sizes.append(int(line))

# ---
# ----------------------------
def model_cpsat(prob:Problem):

    model = cp_model.CpModel()

    x = {}
    for i in range(prob.num_items):
        for j in range(prob.max_bins):
            x[i,j] = model.new_bool_var(f'x_{i}_{j}')

    y = {}
    for i in range(prob.max_bins):
        y[i] = model.new_bool_var(f'y_{i}')

    for i in range(prob.num_items):
        model.add(sum(x[i,j] for j in range(prob.max_bins)) == 1)

    for j in range(prob.max_bins):
        model.add(sum(prob.sizes[i] * x[i,j]
                    for i in range(prob.num_items)) <= y[j] * prob.capacity)

    obj = model.new_int_var(0, prob.max_bins, 'obj')
    obj = sum([y[j] for j in range(prob.max_bins)])
    model.minimize(obj)

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = 10*60

    print('solving...')
    status = solver.Solve(model)

    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        print(f'status: {solver.StatusName(status)}')
        print(f'time={solver.WallTime():.1f}')
        print(f'obj={int(solver.objective_value())}')
    else:
        print('No solution found.')
        print(f'Status: {solver.StatusName(status)}')


# ----
# --------------------------
def model_mip(prob:Problem):

    solver = pywraplp.Solver.CreateSolver('SCIP')
    # solver = pywraplp.Solver.CreateSolver('BOP')
    # solver = pywraplp.Solver.CreateSolver('CBC')

    x = {}
    for i in range(prob.num_items):
        for j in range(prob.max_bins):
            x[i,j] = solver.BoolVar(f'x_{i}')

    y = {}
    for i in range(prob.max_bins):
        y[i] = solver.BoolVar(f'y_{i}')

    for i in range(prob.num_items):
        solver.Add(sum(x[i,j] for j in range(prob.max_bins)) == 1)

    for j in range(prob.max_bins):
        solver.Add(sum(prob.sizes[i] * x[i,j]
                    for i in range(prob.num_items)) <= y[j] * prob.capacity)

    obj = solver.IntVar(0, prob.max_bins, 'obj')
    obj = sum([y[j] for j in range(prob.max_bins)])
    solver.Minimize(obj)

    solver.EnableOutput()
    solver.SetTimeLimit(10*60*1000) # 10 minutes

    print(f"solving with {solver.SolverVersion()}...")
    status = solver.Solve()

    if status in [pywraplp.Solver.OPTIMAL, pywraplp.Solver.FEASIBLE]:
        print(f'status: {status}')
        print(f'obj={int(solver.Objective().Value()):,}')
        print(f'time={solver.WallTime():.1f}')
    else:
        print('No solution found.')
        print(f'status: {status}')


if __name__ == "__main__":
    prob = Problem("day8/prob1.txt")

    # print(prob.name, prob.capacity, prob.num_items,
    #         prob.max_bins, len(prob.sizes))
    # print(prob.sizes[0])
    # print(prob.sizes[1])
    # print(prob.sizes[-2])
    # print(prob.sizes[-1])

    # do binary search to find best value for max_bins
    # between upper and lower bound
    # upper bound = prob.num_items
    # lower bound = sum(prob.sizes) // prob.capacity + 1
    # try max_bins = 120, 60, 30, 45, 52, 48 (47)
    # prob.max_bins = ...
    # model_cpsat(prob)
    
    # model_mip(prob)
