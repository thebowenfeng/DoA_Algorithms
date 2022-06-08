from graph_utils import Node, Graph, print_graph, display_edge
from tree_utils import DELIMITER


def dijkstra(graph: Graph, start_node: Node, end_node: Node):
    print("Performing Dijkstra's algorithm on the following graph:")
    print_graph(graph)

    distances = {}
    for node in graph.node_list:
        distances[id(node)] = float("inf")

    traversed = [start_node]
    total_dist = 0

    curr_node = start_node
    distances[id(curr_node)] = 0

    has_finished = False
    while not has_finished:
        print(DELIMITER)
        print(f"The current node: {curr_node} has the following connections: {[display_edge(i) for i in curr_node.connections]}")

        for edge in curr_node.connections:
            if edge[1] not in traversed and distances[id(curr_node)] + edge[2] < distances[id(edge[1])]:
                distances[id(edge[1])] = distances[id(curr_node)] + edge[2]

        #Find smallest distance currently to travel to
        min_val = float("inf")
        min_node = None
        for edge in curr_node.connections:
            if edge[1] not in traversed and (min_node is None or edge[2] < min_val):
                min_val = edge[2]
                min_node = edge[1]

        curr_node = min_node
        traversed.append(curr_node)
        print("The closest node to the current node is: {}, with distance of {} from the starting point. We will travel to {}".format(curr_node, min_val, curr_node))

        if curr_node == end_node:
            total_dist = min_val
            has_finished = True

    print(f"The overall traverse path is {[str(i) for i in traversed]}, with cost of {total_dist}")