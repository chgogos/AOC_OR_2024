'''
instance: u120_00
--- CP_SAT ---
    49 bins, status: OPTIMAL
    time=1.2
    48 bins, status: OPTIMAL
    time=149.6
    47 bins, No solution found.
    Status: INFEASIBLE, walltime: 0.810061

--- CBC ---

--- SCIP ---
    49 bins, CIP Status        : problem is solved [optimal solution found]
    Solving Time (sec) : 46.00
    48 bins, SCIP Status        : problem is solved [optimal solution found]
    Solving Time (sec) : 266.00
    47 bins, SCIP Status        : problem is solved [infeasible]
    Solving Time (sec) : 0.00
# '''
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

    for i in range(prob.num_items):
        model.add(sum(x[i,j] for j in range(prob.max_bins)) == 1)

    for j in range(prob.max_bins):
        model.add(sum(prob.sizes[i] * x[i,j]
                    for i in range(prob.num_items)) <= prob.capacity)

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = 10*60

    print('solving...')
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'status: {solver.StatusName(status)}')
        print(f'time={solver.WallTime():.1f}')
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

    for i in range(prob.num_items):
        solver.Add(sum(x[i,j] for j in range(prob.max_bins)) == 1)

    for j in range(prob.max_bins):
        solver.Add(sum(prob.sizes[i] * x[i,j]
                    for i in range(prob.num_items)) <= prob.capacity)
    print('solving...')
    solver.EnableOutput()
    solver.SetTimeLimit(5*60*1000) # 5 minutes

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print(f'status: {status}')
        # print(f'obj={int(solver.Objective().Value()):,}')
        # print(f'time={solver.WallTime():.1f}')
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

    prob.max_bins = 47
    model_cpsat(prob)
    # model_mip(prob)
