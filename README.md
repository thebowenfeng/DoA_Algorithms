# DoA_Algorithms

List of DoA algorithms and data structures, with detailed logging of the process of each algorithm/data structure.

Sample usage of each algorithm/data structure is in main.py

## Trees

##### AVL Tree

`insert_avl_tree()` and `delete_avl_tree()` in `AVL.py`. 

##### 2-3 Trees

`insert_23_tree()` in `twothreetree.py`

## Graph algorithms

Graphs can be undirected and weighted. Specify when constructing graph.

##### Prim's Algorithm

`prims()` in `prim.py`

##### Dijkstra's Algorithm

`dijkstra()` in `dijkstra.py`

##### Warshall's Algorithm

Only for finding transitive closure of graph

`warshall()` in `floyd_warshall.py`

##### Floyd's (Floyd-Warshall's) Algorithm

`floyd()` in `floyd_warshall.py`

## Compression

##### Huffman Encoding

`huffman()` and `huffman_decode()` in `huffman.py`

## HashTable

`HashTable.insert()` and `HashTable.lookup()` in `hash_tables.py`

## String search

`horspool()` in `horspool.py`

## Heap

Heap is assumed to be max heap

`heapify()`, `insert_heap()`, `delete_heap()` in `heap.py`

## Sorting algorithms

##### Heap sort

`heap_sort()` in `heap.py`

##### Quick sort

Quicksort assumes lomuto partitioning scheme

`quicksort()` in `quicksort.py`

##### Merge sort

`mergesort()` in `mergesort.py`

##### Radix sort

Radix sort assumes base 10 and sorting on LSD.

`radixsort()` in `radixsort.py`
