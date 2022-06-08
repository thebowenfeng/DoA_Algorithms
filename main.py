from AVL import insert_avl_tree, delete_avl_tree
from twothreetree import insert_23_tree
from graph_utils import Node, Graph
from prims import prims

if __name__ == '__main__':
    #data = [1,2,3,4,5,6,7,8,9,10,11]
    #root = insert_avl_tree(data)

    #to_delete = [5,6,7,8,9,10,11]
    #root = delete_avl_tree(root, to_delete)

    #data = ['C', 'O', 'M', 'P', 'L', 'E', 'X', 'I', 'T', 'Y']

    #root = insert_23_tree(data)

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    graph = Graph()

    graph.add_edge(node1, node6, 10)
    graph.add_edge(node1, node2, 28)
    graph.add_edge(node2, node3, 16)
    graph.add_edge(node2, node7, 14)
    graph.add_edge(node3, node4, 12)
    graph.add_edge(node4, node7, 18)
    graph.add_edge(node4, node5, 22)
    graph.add_edge(node5, node6, 25)
    graph.add_edge(node5, node7, 24)

    prims(graph)

