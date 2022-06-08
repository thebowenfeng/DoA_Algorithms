class Node:
    def __init__(self, data):
        self.data = data
        self.connections = []

    def add_connection(self, node, weight=1):
        self.connections.append((self, node, weight))

    def __str__(self):
        return f"Node {self.data}"


class Graph:
    def __init__(self):
        self.node_list = []
        self.edge_list = []

    def add_edge(self, node1: Node, node2: Node, weight=1):
        if node1 not in self.node_list:
            self.node_list.append(node1)
        if node2 not in self.node_list:
            self.node_list.append(node2)

        node1.add_connection(node2, weight)
        node2.add_connection(node1, weight)
        self.edge_list.append((node1, node2, weight))


def display_edge(edge):
    return f"({edge[0]} to {edge[1]}. Weight: {edge[2]})"


def print_graph(graph: Graph):
    for node in graph.node_list:
        print(f"{node}. Edges: {[display_edge(i) for i in node.connections]}")