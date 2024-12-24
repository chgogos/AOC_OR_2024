'''
--- CP_SAT ---

--- CBC ---
# '''
from collections import defaultdict

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
                self.tasks_num = int(items[0])
                self.time = int(items[1])
                self.crews = 35
            break

        self.tasks = {}
        for aa,line in enumerate(lines[i+1:i+1+self.tasks_num]):
            line = line.strip()
            if len(line)==0:
                continue

            items = line.split()
            self.tasks[aa] = [int(x) for x in items]

        self.links_list = []
        for aa,line in enumerate(lines[i+1+self.tasks_num:]):
            line = line.strip()
            if len(line)==0:
                continue

            items = line.split()
            self.links_list.append((int(items[0])-1,int(items[1])-1,int(items[2])))

# ----
# --------------------------
def model_mip(prob:Problem):

    # solver = pywraplp.Solver.CreateSolver('SCIP')
    # solver = pywraplp.Solver.CreateSolver('CPLEX')
    solver = pywraplp.Solver.CreateSolver('CBC')

    # trips with one task
    cols1 = prob.tasks_num

    # trips with two tasks
    cols2 = len(prob.links_list)
    cols = cols1 + cols2

    # solve a Set Partition Problem
    x = {}
    for i in range(cols):
        x[i] = solver.BoolVar(f'x_{i}')

    for i in range(prob.tasks_num):
        x_list = [x[i]]
        for aa,(t1,t2,_) in enumerate(prob.links_list):
            if t1==i:
                x_list.append(x[cols1+aa])
            if t2==i:
                x_list.append(x[cols1+aa])

        solver.Add(sum(x_list) == 1)

    # max number of crews
    solver.Add(sum(x[i] for i in range(cols1)) +
                        sum(x[cols1+i] for i in range(cols2)) <= prob.crews)

    obj = solver.IntVar(0, 1_000_000, "obj")
    solver.Add(obj == sum(prob.tasks[i][0] * x[i] for i in range(cols1)) +
                        sum(prob.links_list[i][2] * x[cols1+i] for i in range(cols2)))

    solver.Minimize(obj)

    print('solving...')
    solver.EnableOutput()
    solver.SetTimeLimit(prob.time*60*1000) # prob.times minutes

    status = solver.Solve()

    if status in [pywraplp.Solver.OPTIMAL, pywraplp.Solver.FEASIBLE]:
        print(f'status: {status}')
        print(f'obj={int(solver.Objective().Value()):,}')
        # print(f'time={solver.WallTime():.1f}')
        cnum = 1
        for i in range(cols1):
            if x[i].solution_value() > 0:
                print(f'crew_{cnum}: task -> {i+1}')
                cnum += 1
        for i in range(cols2):
            if x[cols1+i].solution_value() > 0:
                print(f'crew_{cnum}: tasks -> {prob.links_list[i][0]+1},{prob.links_list[i][1]+1}')
                cnum += 1
    else:
        print('No solution found.')
        print(f'status: {status}')


if __name__ == "__main__":
    prob = Problem("day16/instance_16.txt")

    # print(prob.tasks_num, prob.time, prob.crews)
    # print(prob.tasks[0])
    # print(prob.tasks[prob.tasks_num-1])
    # print(prob.links[0])
    # print(prob.links[46])

    model_mip(prob)
