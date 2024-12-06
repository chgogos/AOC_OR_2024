from ortools.sat.python import cp_model
from ortools.linear_solver import pywraplp

class Problem:
    def __init__(self, fn):

        with open(fn, "r") as f:
            lines = f.readlines()

        for i,line in enumerate(lines):
            line = line.strip()
            if len(line)==0 or line.startswith("#"):
                continue

            items = line.split()
            if len(items) == 2:
                self.segments = int(items[0])
                self.possibilities = int(items[1])
            break

        self.cost_segments = []
        for line in lines[i+1:]:
            line = line.strip()
            if len(line)==0:
                continue
        
            items = line.split()
            c = int(items[0])
            self.cost_segments.append((c, [int(x) for x in items[1:]]))

# ----
# ----------------------------
def model_cpsat(prob:Problem):

    model = cp_model.CpModel()

    x = {}
    for i in range(prob.possibilities):
        x[i] = model.NewBoolVar(f'x_{i}')

    for i in range(prob.segments):
        x_list = []
        for j, (c, seg_list) in enumerate(prob.cost_segments):
            if i+1 in seg_list:
                x_list.append(x[j])

        if len(x_list) == 0:
            print(f'no x_list for segment={i+1}')
            exit(0)

        model.add(sum(x_list) >= 1)

    obj = model.NewIntVar(0, 1_000_000, "obj")
    model.add(obj == sum(c * x[i] for i,(c,_) in enumerate(prob.cost_segments)))

    model.minimize(obj)

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = 5*60

    print('solving...')
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'status: {solver.StatusName(status)}')
        print(f'obj={int(solver.ObjectiveValue()):,}')
        print(f'bound={int(solver.BestObjectiveBound()):,}')
        print(f'time={solver.WallTime():.1f}')
    else:
        print('No solution found.')
        print(f'Status: {solver.StatusName(status)}')


# ----
# --------------------------
def model_mip(prob:Problem):

    # solver = pywraplp.Solver.CreateSolver('SCIP')
    # solver = pywraplp.Solver.CreateSolver('CPLEX')
    solver = pywraplp.Solver.CreateSolver('CBC')

    x = {}
    for i in range(prob.possibilities):
        x[i] = solver.BoolVar(f'x_{i}')

    for i in range(prob.segments):
        x_list = []
        for j, (c, seg_list) in enumerate(prob.cost_segments):
            if i+1 in seg_list:
                x_list.append(x[j])

        if len(x_list) == 0:
            print(f'no x_list for segment={i+1}')
            exit(0)

        solver.Add(sum(x_list) >= 1)

    obj = solver.IntVar(0, 1_000_000, "obj")
    solver.Add(obj == sum(c * x[i] for i,(c,_) in enumerate(prob.cost_segments)))

    solver.Minimize(obj)

    print('solving...')
    solver.EnableOutput()
    solver.SetTimeLimit(5*60*1000) # 5 minutes

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print(f'status: {status}')
        print(f'obj={int(solver.Objective().Value()):,}')
        # print(f'time={solver.WallTime():.1f}')
    else:
        print('No solution found.')
        print(f'status: {status}')


if __name__ == "__main__":
    prob = Problem("day6/instance.txt")

    # print(prob.segments, prob.possibilities)
    # print(prob.cost_segments[0])
    # print(prob.cost_segments[-1])

    model_cpsat(prob)
    # model_mip(prob)


'''
--- CP_SAT ---
#13    186.88s best:169   next:[167,168]  pseudo_costs (fixed_bools=1/46662)
#Bound 272.70s best:169   next:[168,168]

--- CBC ---
Objective value:                169.00000000
Lower bound:                    166.784
Gap:                            0.01
Enumerated nodes:               5185
Total iterations:               1064724
Time (CPU seconds):             299.99
Time (Wallclock seconds):       299.99

Total time (CPU seconds):       300.00   (Wallclock seconds):       300.00
# '''
