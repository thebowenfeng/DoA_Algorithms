from graph_utils import Graph, Node, print_graph
from tree_utils import DELIMITER


def print_table(graph: Graph, table):
    print(f"{' ' * 7}| {' '.join([str(i) for i in graph.node_list])}")
    for i in range(len(table)):
        print(f"{graph.node_list[i]} | {table[i]}")


def warshall(graph: Graph):
    print(f"Performing warshall (transitive closure) on graph:")
    print_graph(graph)

    table = []
    for i in range(len(graph.node_list)):
        table.append([])
        for j in range(len(graph.node_list)):
            table[i].append(False)

    # Initial direct edges
    for index, node in enumerate(graph.node_list):
        table[index][index] = True
        for edge in node.connections:
            print(f"Direct path from {node} to {edge[1]} exists.")
            table[index][graph.node_list.index(edge[1])] = True

    print(f"Current table: ")
    print_table(graph, table)

    for index, node in enumerate(graph.node_list):
        print(DELIMITER)
        print(f"Setting {node} as the middle node.")

        for i in range(len(table)):
            if i == index:
                continue
            for j in range(len(table[i])):
                if j == index or i == j:
                    continue

                if not table[i][j] and table[i][index] and table[index][j]:
                    print(f"Path from {graph.node_list[i]} to {graph.node_list[j]} did not exist. However, path from {graph.node_list[i]} to {graph.node_list[index]} and {graph.node_list[index]} to {graph.node_list[j]} exist")
                    table[i][j] = True
        print("Current table: ")
        print_table(graph, table)


def floyd(graph: Graph):
    print(f"Performing floyd (floyd-warshall) on graph:")
    print_graph(graph)

    table = []
    for i in range(len(graph.node_list)):
        table.append([])
        for j in range(len(graph.node_list)):
            table[i].append(float('inf'))

    # Initial direct edges
    for index, node in enumerate(graph.node_list):
        table[index][index] = 0
        for edge in node.connections:
            print(f"Direct path from {node} to {edge[1]} with weight {edge[2]} exists.")
            table[index][graph.node_list.index(edge[1])] = edge[2]

    print(f"Current table: ")
    print_table(graph, table)

    for index, node in enumerate(graph.node_list):
        print(DELIMITER)
        print(f"Setting {node} as the middle node.")

        for i in range(len(table)):
            if i == index:
                continue
            for j in range(len(table[i])):
                if j == index or i == j:
                    continue

                if table[i][index] + table[index][j] < table[i][j]:
                    print(
                        f"Smaller path from {graph.node_list[i]} to {graph.node_list[index]} with weight {table[i][index]} and {graph.node_list[index]} to {graph.node_list[j]} with weight {table[index][j]} exist")
                    table[i][j] = table[i][index] + table[index][j]

        print("Current table: ")
        print_table(graph, table)
