import os
from collections import defaultdict
from ortools.sat.python import cp_model


def read_problem_instance(problem_instance_fn):
    with open(problem_instance_fn, "r") as f:
        first_line = True
        conflicts = []
        for line in f:
            if line.strip() == "":
                continue
            if line[0] == "#":
                continue
            if first_line:
                number_of_events, number_of_conflicts = [int(x) for x in line.split()]
                first_line = False
            else:
                _, e1, e2 = line.split()
                conflicts.append((int(e1), int(e2)))
        print(f"{number_of_events=}, {number_of_conflicts=}")
        # print(conflicts)
        return number_of_events, number_of_conflicts, conflicts


def solve(number_of_events, conflicts, time_limit=120):
    model = cp_model.CpModel()
    dvars = {}
    for i in range(number_of_events):
        event_index = i + 1
        dvars[event_index] = model.new_int_var(1, number_of_events, f"e{event_index}")
    print(dvars)
    for e1, e2 in conflicts:
        model.add(dvars[e1] != dvars[e2])

    max_dvar = model.new_int_var(0, 100, "max_dvar")
    model.add_max_equality(target=max_dvar, exprs=dvars.values())

    model.minimize(max_dvar)

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = time_limit
    status = solver.solve(model)

    print("\nStatistics")
    print(f"  status   : {solver.status_name(status)}")
    print(f"  conflicts: {solver.num_conflicts}")
    print(f"  branches : {solver.num_branches}")
    print(f"  wall time: {solver.wall_time} s")

    # display solution
    print(f"Rooms needed = {int(solver.objective_value)}")
    rooms_events = defaultdict(list)
    for i in range(number_of_events):
        event_index = i + 1
        rooms_events[solver.value(dvars[event_index])].append(event_index)
        # print(f"Event {event_index} is scheduled at {solver.value(dvars[event_index])}")
    for room_id in sorted(rooms_events):
        events = rooms_events[room_id]
        print(f"{room_id}: {events}")


if __name__ == "__main__":
    fn = os.path.join(os.path.dirname(__file__), "instance.txt")
    number_of_events, _, conflicts = read_problem_instance(fn)
    solve(number_of_events, conflicts, 60)
