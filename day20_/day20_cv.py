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
                self.locations = int(items[0])
                self.best_cost = int(items[1])
            break

        self.flow = [[None for _ in range(self.locations)] for _ in range(self.locations)]
        for j, line in enumerate(lines[i+1:i+1+self.locations]):
            line = line.strip()
            items = line.split()
            for k in range(self.locations):
                self.flow[j][k] = int(items[k])

        self.distance = [[None for _ in range(self.locations)] for _ in range(self.locations)]
        for j, line in enumerate(lines[i+2+self.locations:]):
            line = line.strip()
            items = line.split()
            for k in range(self.locations):
                self.distance[j][k] = int(items[k])


# ----
# ----------------------------
def model_cpsat(prob:Problem):

    model = cp_model.CpModel()

    # various departments:
    # Emergency Room
    # Radiology and Operating Room
    # Pharmacy Room
    # ICU (Intensive Care Unit) Room
    # Laboratory Room
    # ...

    x = {}
    for i in range(prob.locations):
        for j in range(prob.locations):
            x[i,j] = model.NewBoolVar(f'x_{i}_{j}')

    # at each location one department
    for i in range(prob.locations):
        model.add(sum(x[i,j] for j in range(prob.locations)) == 1)

    # each department at one location
    for j in range(prob.locations):
        model.add(sum(x[i, j] for i in range(prob.locations)) == 1)

    # So we started addressing this problem considering two factors:
    # The flow of movements between different departments
    # The distance we have between them
    # And with that information, we're building the travel costs.

    obj = model.NewIntVar(0, 1_000_000_000, "obj")
    model.add(obj == sum((sum(prob.flow[i][j] * prob.distance[i][j]
                                for j in range(prob.locations))) * x[i,j]
                            for i in range(prob.locations)
                            for j in range(prob.locations)))

    model.minimize(obj)

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = 5*60

    print('solving...')
    status = solver.Solve(model)

    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        print(f'status: {solver.StatusName(status)}')
        print(f'obj={int(solver.ObjectiveValue()):,}')
        print(f'bound={int(solver.BestObjectiveBound()):,}')
        print(f'time={solver.WallTime():.1f}')

        for i in range(prob.locations):
            for j in range(prob.locations):
                if solver.Value(x[i,j]):
                    print(f'location {i:2d}: department: {j:2d}')

    else:
        print('No solution found.')
        print(f'Status: {solver.StatusName(status)}')

# ------------------------
if __name__ == "__main__":
    prob = Problem("day20_/instance.txt")

    # print(prob.locations, prob.best_cost)
    # print(prob.flow[0][0],prob.flow[0][25])
    # print(prob.distance[0][0],prob.distance[0][25])
    # print(prob.distance[25][0],prob.distance[25][25])

    model_cpsat(prob)
    # model_mip(prob)
