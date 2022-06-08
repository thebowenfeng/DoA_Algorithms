from graph_utils import Node, Graph, print_graph, display_edge
from tree_utils import DELIMITER


def find_min_edge(graph: Graph):
    min_edge = None
    for edge in graph.edge_list:
        if min_edge is None or edge[2] < min_edge[2]:
            min_edge = edge
    return min_edge


def prims(graph: Graph):
    print("Performing Prim's algorithm on the following graph:")
    print_graph(graph)

    min_edge = find_min_edge(graph)
    traversed = [min_edge[0], min_edge[1]]
    visited_edges = [min_edge]

    print("Minimum edge selected in the graph, edge: ", display_edge(min_edge))

    curr_node1: Node = min_edge[0]
    curr_node2: Node = min_edge[1]

    print("Starting Prim's algorithm with {} and {}".format(curr_node1, curr_node2))

    has_finished = False
    while not has_finished:
        print(DELIMITER)
        print(f"{curr_node1} has the following connections: {[display_edge(i) for i in curr_node1.connections]}")
        print(f"{curr_node2} has the following connections: {[display_edge(i) for i in curr_node2.connections]}")

        min_edge = None
        for edge in curr_node1.connections:
            if edge[1] not in traversed and (min_edge is None or edge[2] < min_edge[2]):
                min_edge = edge

        for edge in curr_node2.connections:
            if edge[1] not in traversed and (min_edge is None or edge[2] < min_edge[2]):
                min_edge = edge

        if min_edge is None:
            print("All connecting nodes to the 2 nodes have been traversed. Minimum spanning tree has been found.")
            has_finished = True
        else:
            print(f"Minimum edge selected in the graph, edge: {display_edge(min_edge)}")
            traversed.append(min_edge[1])
            visited_edges.append(min_edge)

            if min_edge[0] == curr_node1:
                print(f"{curr_node1} has been replaced by {min_edge[1]}")
                curr_node1 = min_edge[1]
            else:
                print(f"{curr_node2} has been replaced by {min_edge[1]}")
                curr_node2 = min_edge[1]

    print(f"All traversed: {[display_edge(i) for i in visited_edges]}")
    print(f"Total cost of minimum spanning tree: {sum([i[2] for i in visited_edges])}")
    return sum([i[2] for i in visited_edges])