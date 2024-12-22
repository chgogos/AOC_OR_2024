import os
import logging
import networkx as nx
import matplotlib.pyplot as plt


class Problem:
    def __init__(self, number_of_nodes, number_of_edges):
        self.number_of_nodes = number_of_nodes
        self.number_of_edges = number_of_edges
        self.nodes = []
        self.edges = []
        self.mandatory_nodes = []

    def add_edge(self, node1, node2, cost):
        self.edges.append((node1, node2, cost))

    def display_info(self):
        logging.info(f"# nodes = {self.number_of_nodes}")
        logging.info(f"mandatory nodes = {self.mandatory_nodes}")
        logging.info(f"# edges = {self.number_of_edges}")

    def convert_to_nx_graph(self):
        G = nx.Graph()
        for node in self.nodes:
            G.add_node(node)
        for edge in self.edges:
            G.add_edge(edge[0], edge[1], weight=edge[2])
        return G


def read_problem_data(fn):
    with open(fn, "r") as f:
        file_section = "A"
        edge_counter = 0
        for line in f:
            if line[0] == "#":
                continue
            if str(line).strip() == "":
                continue
            if file_section == "A":
                number_of_nodes, number_of_edges = line.split()
                a_problem = Problem(int(number_of_nodes), int(number_of_edges))
                file_section = "B"
                continue
            if file_section == "B":
                v = line.split()
                a_problem.add_edge(int(v[0]), int(v[1]), int(v[2]))
                edge_counter += 1
                if edge_counter == a_problem.number_of_edges:
                    file_section = "C"
                    continue
            if file_section == "C":
                number_of_mandatory_nodes = int(line)
                file_section = "D"
                continue
            if file_section == "D":
                a_problem.mandatory_nodes = [int(x) for x in line.split()]
    return a_problem


def solve(a_problem):
    G = a_problem.convert_to_nx_graph()
    T = nx.algorithms.approximation.steiner_tree(
        G, a_problem.mandatory_nodes, weight="weight", method=None
    )

    logging.info(f"Minimum spanning tree: {T.edges(data=True)}")
    logging.info(
        f"Total cost: {sum([data['weight'] for _, _, data in T.edges(data=True)])}"
    )

    # Visualize the graph and the minimum spanning tree
    pos = nx.spring_layout(T)
    nx.draw_networkx_nodes(
        T, pos, nodelist=a_problem.mandatory_nodes, node_color="orange", node_size=700
    )
    nx.draw_networkx_nodes(
        T,
        pos,
        nodelist=[node for node in T.nodes if node not in a_problem.mandatory_nodes],
        node_color="lightblue",
        node_size=500,
    )

    # nx.draw_networkx_edges(T, pos, edge_color="grey")
    nx.draw_networkx_labels(T, pos, font_size=12, font_family="sans-serif")
    nx.draw_networkx_edge_labels(
        T, pos, edge_labels={(u, v): d["weight"] for u, v, d in T.edges(data=True)}
    )
    nx.draw_networkx_edges(T, pos, edge_color="green", width=2)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    fn = os.path.join(os.path.dirname(__file__), "instance.txt")
    a_problem = read_problem_data(fn)
    a_problem.display_info()
    solve(a_problem)
