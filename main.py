from AVL import insert_avl_tree, delete_avl_tree, Node
from twothreetree import insert_23_tree
#from graph_utils import Node, Graph
from prims import prims
from dijkstras import dijkstra
from huffman import huffman, huffman_decode
from hash_tables import HashTable
from horspool import horspool
from heap import heapify, heap_delete, heap_sort
from quicksort import quicksort, lomuto
from mergesort import mergesort
from floyd_warshall import warshall, floyd

if __name__ == '__main__':
    '''
    # data = [1,2,3,4,5,6,7,8,9,10,11]
    # root = insert_avl_tree(data)

    # to_delete = [5,6,7,8,9,10,11]
    # root = delete_avl_tree(root, to_delete)

    # data = ['C', 'O', 'M', 'P', 'L', 'E', 'X', 'I', 'T', 'Y']
    # root = insert_23_tree(data)
    
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
    
    graph = Graph()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    graph.add_edge(node1, node2, 2, False)
    graph.add_edge(node1, node3, 4, False)
    graph.add_edge(node2, node3, 1, False)
    graph.add_edge(node2, node4, 7, False)
    graph.add_edge(node3, node5, 3, False)
    graph.add_edge(node5, node4, 2, False)
    graph.add_edge(node4, node6, 1, False)
    graph.add_edge(node5, node6, 5, False)

    dijkstra(graph, node1, node4)
    
    # en_msg, encoding = huffman("free-coffee")
    # de_msg = huffman_decode(en_msg, encoding)

    table = HashTable(8, hash_func=lambda x: x % 8, mode="separate_chaining")

    table.insert(9, "one")
    table.insert(17, "two")
    table.insert(4, "three")
    table.insert(11, "four")
    table.insert(1, "five")

    table.lookup(15)
    
    # horspool("trusthardtoothbrushes", "tooth")

    # arr = [None, 8, 4, 3, 5, 2, 13, 6, 4]
    # heapify(arr)
    # print(heap_delete(arr))
    
    # arr = [None, 8, 4, 3, 5, 2, 13, 6, 4]
    # new = heap_sort(arr)
    # print(new)
    
    # print(quicksort([1, 7, 6, 2, 9, 4, 3, 5]))
    
    # print(mergesort([1, 7, 6, 2, 9, 4, 3, 5]))
    
    # print(radixsort([237, 146, 259, 348, 152, 163, 235, 48, 36, 62]))
    
    graph = Graph()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    graph.add_edge(node1, node2, 3, False)
    graph.add_edge(node2, node3, 2, False)
    graph.add_edge(node1, node4, 7, False)
    graph.add_edge(node2, node1, 8, False)
    graph.add_edge(node3, node1, 5, False)
    graph.add_edge(node3, node4, 1, False)
    graph.add_edge(node4, node1, 2, False)
    
    warshall(graph)
    floyd(graph)
    '''
    
