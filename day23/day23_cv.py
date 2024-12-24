from ortools.sat.python import cp_model
from ortools.linear_solver import pywraplp

class Problem:
    def __init__(self, fn):

        with open(fn, "r", encoding='utf-8') as f:
            lines = f.readlines()

        for i,line in enumerate(lines):
            line = line.strip()
            if len(line)==0 or line.startswith("#"):
                continue

            items = line.split()
            if len(items) == 2:
                self.products = int(items[0])
                self.select = int(items[1])
            break

        self.distance = [[0 for _ in range(self.products)] for _ in range(self.products)]
        for line in lines[i+1:]:
            items = line.strip().split()
            m,k = int(items[0]), int(items[1])
            self.distance[m][k] = int(float(items[2])*10**5)
            self.distance[k][m] = int(float(items[2])*10**5)

# ----
# ----------------------------
def model_cpsat(prob:Problem):

    model = cp_model.CpModel()

    x = {(i,j): model.NewBoolVar(f'x_{i}_{j}')
            for i in range(prob.products)
            for j in range(i+1,prob.products)}

    b = {i: model.NewBoolVar(f'b_{i}')
            for i in range(prob.products)}

    model.add(sum(x[i,j]
            for i in range(prob.products)
            for j in range(i+1,prob.products)) == prob.select*(prob.select-1)//2)

    for i in range(prob.products):
        for j in range(i+1,prob.products):
            model.add(b[i] >= x[i, j])
            model.add(b[j] >= x[i, j])

    model.add(sum(b[i] for i in range(prob.products)) == prob.select)

    ub = sum(prob.distance[i][j]
                for i in range(prob.products)
                for j in range(i+1, prob.products))
    obj = model.NewIntVar(0, ub, "obj")
    model.add(obj == sum(prob.distance[i][j] * x[i, j]
                                for i in range(prob.products)
                                for j in range(i+1,prob.products)))

    model.maximize(obj)

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = 5*60

    print('solving...')
    status = solver.Solve(model)

    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        print(f'status: {solver.StatusName(status)}')
        print(f'obj  ={int(solver.ObjectiveValue()):,} / 100_000')
        print(f'bound={int(solver.BestObjectiveBound()):,} / 100_000')
        print(f'time ={solver.WallTime():.1f}')

        print(f'selected products:{[i for i in range(prob.products)
                                    if solver.value(b[i])]}')

        num,tot = 0,0
        for i in range(prob.products):
            for j in range(i+1,prob.products):
                if solver.Value(x[i,j]):
                    dist = prob.distance[i][j]/100_000
                    print(f'{num+1:2d}: product {i:2d}: product: {j:2d} {dist=}')
                    num += 1
                    tot += dist
        print(f'{tot=:.5f}')
    else:
        print('No solution found.')
        print(f'Status: {solver.StatusName(status)}')

# ----
# --------------------------
def model_mip(prob:Problem):

    # solver = pywraplp.Solver.CreateSolver('SCIP')
    # solver = pywraplp.Solver.CreateSolver('BOP')
    solver = pywraplp.Solver.CreateSolver('CBC')

    x = {(i,j): solver.BoolVar(f'x_{i}_{j}')
            for i in range(prob.products)
            for j in range(prob.products)}

    b = {i: solver.BoolVar(f'b_{i}')
            for i in range(prob.products)}

    solver.Add(sum(x[i,j]
            for i in range(prob.products)
            for j in range(i+1,prob.products)) == prob.select*(prob.select-1)//2)

    for i in range(prob.products):
        for j in range(i+1, prob.products):
            solver.Add(b[i] >= x[i, j])
            solver.Add(b[j] >= x[i, j])

    solver.Add(sum(b[i] for i in range(prob.products)) == prob.select)

    ub = sum(prob.distance[i][j]
                for i in range(prob.products)
                for j in range(i+1, prob.products))
    obj = solver.IntVar(0, ub, 'obj')
    obj = sum([prob.distance[i][j] * x[i,j]
                    for i in range(prob.products)
                    for j in range(i+1,prob.products)])

    solver.Maximize(obj)

    solver.EnableOutput()
    solver.SetTimeLimit(10*60*1000) # 10 minutes

    print(f"solving with {solver.SolverVersion()}...")
    status = solver.Solve()

    if status in [pywraplp.Solver.OPTIMAL, pywraplp.Solver.FEASIBLE]:
        print(f'status: {status}')
        print(f'obj={int(solver.Objective().Value()):,} / 100_000')
        print(f'time={solver.WallTime()/1000:.1f}')

        print(f'selected products:{[i for i in range(prob.products)
                                    if b[i].solution_value()]}')
    else:
        print('No solution found.')
        print(f'status: {status}')

# ------------------------
if __name__ == "__main__":
    prob = Problem("day23/instance.txt")

    # print(prob.products, prob.select)
    # print(prob.distance[0])
    # print(prob.distance[-1])

    model_cpsat(prob)
    # model_mip(prob)
