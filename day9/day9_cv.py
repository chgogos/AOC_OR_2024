'''
--- CP_SAT ---
# '''
from ortools.sat.python import cp_model
from ortools.linear_solver import pywraplp

import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Problem:
    def __init__(self, fn):

        with open(fn, "r") as f:
            lines = f.readlines()

        self.objects = []
        self.items = []
        for i,line in enumerate(lines):
            line = line.strip()
            if len(line)==0:
                continue

            if  line.startswith("# objects"):
                k = int(lines[i+1].strip())
                for j in range(k):
                    items = lines[i+2+j].strip().split()
                    self.objects.append((int(items[0]), int(items[1]), int(items[2])))

            if  line.startswith("# items"):
                k = int(lines[i+1].strip().split()[0])
                for j in range(k):
                    items = lines[i+2+j].strip().split()
                    self.items.append((int(items[0]), int(items[1])))

    def index_of_object(self, ind):
        n = 0
        for i, o in enumerate(self.objects):
            n += o[2]
            if ind < n:
                return i
        return -1

# ----
# ----------------------------
def model_cpsat(prob:Problem):

    model = cp_model.CpModel()

    num_items = len(prob.items)
    num_objs = sum(x for _,_,x in prob.objects)

    x_ivar, y_ivar, x_var, y_var, isp_var = {}, {}, {}, {}, {}

    for i in range(num_items):
        x_size, y_size = prob.items[i][0], prob.items[i][1]

        for j in range(num_objs):
            k = prob.index_of_object(j)
            x_ub = prob.objects[k][0] - x_size
            y_ub = prob.objects[k][1] - y_size

            x_var[i, j] = model.new_int_var(0, x_ub, f'x_{i}_{j}')
            y_var[i, j] = model.new_int_var(0, y_ub, f'y_{i}_{j}')

            isp_var[i, j] = model.new_bool_var(f'isp_{i}_{j}')

            x_ivar[i, j] = model.new_optional_fixed_size_interval_var(
                    x_var[i,j], x_size, isp_var[i,j], f'xi_{i}_{j}')

            y_ivar[i, j] = model.new_optional_fixed_size_interval_var(
                    y_var[i,j], y_size, isp_var[i,j], f'xi_{i}_{j}')

    for i in range(num_items):
        model.add(sum(isp_var[i,j] for j in range(num_objs)) == 1)

    for j in range(num_objs):
        model.add_no_overlap_2d(
                [x_ivar[i,j] for i in range(num_items)],
                [y_ivar[i,j] for i in range(num_items)])

    # b[j] = 1 if object j is used
    b = {}
    for j in range(num_objs):
        b[j] = model.new_bool_var(f'b_{j}')
        for i in range(num_items):
            model.add(b[j] >= isp_var[i, j])

    # obj = total objects
    obj = model.new_int_var(0, num_objs, 'obj')
    model.add(obj == sum(b[j] for j in range(num_objs)))

    # symmetry (???)
    for j in range(num_objs-1):
        model.add(b[j] >= b[j+1])

    # minimize total used objects
    model.minimize(obj)

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = 2*60

    print('solving...')
    status = solver.Solve(model)

    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        print(f'status: {solver.StatusName(status)}')
        print(f'obj={int(solver.ObjectiveValue())}')
        print(f'bound={int(solver.BestObjectiveBound())}')
        print(f'time={solver.WallTime():.1f}')

        for j in range(num_objs):
            k = prob.index_of_object(j)
            area = prob.objects[k][0] * prob.objects[k][1]
            iarea, titems = 0, 0
            print(f'obj={j+1} x={prob.objects[k][0]} y={prob.objects[k][1]}')
            for i in range(num_items):
                if solver.BooleanValue(isp_var[i,j]):
                    print(f'{i} {prob.items[i]},', end='')
                    iarea += prob.items[i][0] * prob.items[i][1]
                    titems += 1
            print(f'\nitems={titems:2d} area={area} / {iarea} = {100*iarea/area:.1f}%')


        # Create a figure and axes
        # fig, ax = plt.subplots(num_objs//2)#(figsize=(6,6))#(prob.objects[k][0], prob.objects[k][1]))
        fig, ax = plt.subplots(num_objs, 1, figsize=(10, 2 * num_objs))
        for j in range(num_objs):
            k = prob.index_of_object(j)

            ax[j].set_xlim(0, prob.objects[k][0])
            ax[j].set_ylim(0, prob.objects[k][1])
            # ax[j].set_aspect('equal')
            ax[j].set_title(f"Sheet {k+1} ({prob.objects[k][0]}x{prob.objects[k][0]})",
                                fontsize=10)
            ax[j].set_xlabel("Width")
            ax[j].set_ylabel("Height")

            # Add sheet rectangle
            ax[j].add_patch(
                patches.Rectangle(
                    (0, 0), prob.objects[k][0], prob.objects[k][1],
                    edgecolor="black", fill=False, linewidth=2
                )
            )

            # Add items
            for i in range(num_items):
                if solver.BooleanValue(isp_var[i,j]):
                    x, y = solver.Value(x_var[i,j]), solver.Value(y_var[i,j])
                    w, h = prob.items[i][0], prob.items[i][1]
                    rect = patches.Rectangle((x,y), w, h,
                                        # linewidth=1,
                                        edgecolor='r', facecolor='green', alpha=0.6)
                    ax[j].add_patch(rect)

                    ax[j].text(x + w / 2, y + h / 2,
                            f"{i}", ha="center", va="center", fontsize=8, color="black")

            # Set axis limits
            ax[j].set_xlim(0, prob.objects[k][0])
            ax[j].set_ylim(0, prob.objects[k][1])

        # Display the plot
        # plt.grid(True)
        plt.tight_layout()
        plt.show()

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

        solver.Add(sum(x_list) == 1)

    obj = solver.IntVar(0, 1_000_000, "obj")
    solver.Add(obj == sum(c * x[i] for i,(c,_) in enumerate(prob.cost_segments)))

    solver.Minimize(obj)

    print('solving...')
    solver.EnableOutput()
    solver.SetTimeLimit(5*60*1000) # 5 minutes

    status = solver.Solve()

    if status in [pywraplp.Solver.OPTIMAL, pywraplp.Solver.FEASIBLE]:
        print(f'status: {status}')
        print(f'obj={int(solver.Objective().Value()):,}')
        # print(f'time={solver.WallTime():.1f}')
    else:
        print('No solution found.')
        print(f'status: {status}')

# ------------------------
if __name__ == "__main__":
    prob = Problem("day9/m1a.txt")

    # print(prob.objects)
    # print(len(prob.items), prob.items)

    model_cpsat(prob)

    # model_mip(prob)
