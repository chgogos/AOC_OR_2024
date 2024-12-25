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

    b = {i: model.NewBoolVar(f'b_{i}')
            for i in range(prob.products)}

    model.add(sum(b[i] for i in range(prob.products)) == prob.select)

    # ub = sum(prob.distance[i][j]
    #             for i in range(prob.products)
    #             for j in range(i+1, prob.products))
    ub = 1_000_000_000
    obj = model.NewIntVar(0, ub, "obj")

    for i in range(prob.products):
        for j in range(i+1,prob.products):
            model.add(obj <= prob.distance[i][j]).only_enforce_if([b[i],b[j]])

    model.maximize(obj)

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = 5*60

    print('solving...')
    status = solver.Solve(model)

    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        print(f'status: {solver.StatusName(status)}')
        print(f'obj  ={int(solver.ObjectiveValue())/100_000:.5f}')
        print(f'bound={int(solver.BestObjectiveBound())/100_000:.5f}')
        print(f'time ={solver.WallTime():.1f}')

        selected = [i for i in range(prob.products) if solver.value(b[i])]
        print(f'selected products:{selected}')

        for i in selected:
            dist = min(prob.distance[i][j]/100_000
                        for j in selected if j!=i)
            print(f'product {i:2d}: {dist=}')

    else:
        print('No solution found.')
        print(f'Status: {solver.StatusName(status)}')

# ------------------------
if __name__ == "__main__":
    prob = Problem("day23/instance.txt")

    # print(prob.products, prob.select)
    # print(prob.distance[0])
    # print(prob.distance[-1])

    model_cpsat(prob)
