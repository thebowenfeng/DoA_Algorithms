from tree_utils import print_tree, DELIMITER


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


def array_as_tree(arr):
    node_array = [None]
    for i in range(1, len(arr)):
        node_array.append(Node(arr[i]))

    for i in range(1, len(arr)):
        left_ind = 2 * i
        right_ind = 2 * i + 1

        if left_ind < len(arr):
            node_array[i].left = node_array[left_ind]
        if right_ind < len(arr):
            node_array[i].right = node_array[right_ind]

    print_tree(node_array[1], val="value")


def heapify_node(arr, index):
    print(DELIMITER)
    print("Heapifying node:", arr[index])

    left_ind = 2 * index
    right_ind = 2 * index + 1

    # Leaf node
    if left_ind > len(arr) - 1 and right_ind > len(arr) - 1:
        print("Current node is a leaf node (no children). Must be valid heap")
        pass
    else:
        # Only left child
        if right_ind > len(arr) - 1 and arr[left_ind] > arr[index]:
            print(f"Current node only has a left child, and child is bigger than parent. Swapping parent {arr[index]} and child {arr[left_ind]}. Array looks like this:")
            arr[left_ind], arr[index] = arr[index], arr[left_ind]
            array_as_tree(arr)
            print(f"Checking heap validity for the new left child {arr[left_ind]}")
            heapify_node(arr, left_ind)
        elif right_ind < len(arr) and (arr[left_ind] > arr[index] or arr[right_ind] > arr[index]):
            if arr[left_ind] > arr[right_ind]:
                print(f"Left child of node is bigger than parent. Swapping parent {arr[index]} and child {arr[left_ind]}. Array looks like this:")
                arr[left_ind], arr[index] = arr[index], arr[left_ind]
                array_as_tree(arr)
                print(f"Checking heap validity for the new left child {arr[left_ind]}")
                heapify_node(arr, left_ind)
            else:
                print(f"Right child of node is bigger than parent. Swapping parent {arr[index]} and child {arr[right_ind]}. Array looks like this:")
                arr[right_ind], arr[index] = arr[index], arr[right_ind]
                array_as_tree(arr)
                print(f"Checking heap validity for the new right child {arr[right_ind]}")
                heapify_node(arr, right_ind)
        else:
            print(f"Current node is a valid heap. Array looks like this:")
            array_as_tree(arr)


def heapify(arr, zero_index=False):
    if zero_index:
        arr.insert(0, None)

    print(f"Turning array: {arr} into a heap. The array currently looks like this:")
    array_as_tree(arr)

    for i in range(len(arr) -1, 0, -1):
        heapify_node(arr, i)

    print(f"Heapify completed. Array looks like this:")
    array_as_tree(arr)


def heap_insert(heap, val, zero_index=False):
    if zero_index:
        heap.insert(0, None)

    print(f"Inserting {val} into heap {heap}")

    heap.append(val)
    i = len(heap) - 1
    while i > 1:
        print(DELIMITER)
        parent_ind = i // 2
        print(f"Checking if parent {heap[parent_ind]} is bigger than child {heap[i]}")
        if heap[parent_ind] < heap[i]:
            print(f"Swap parent {heap[parent_ind]} and child {heap[i]}. Array now looks like this")
            heap[parent_ind], heap[i] = heap[i], heap[parent_ind]
            array_as_tree(heap)
            i = parent_ind
        else:
            break


def heap_delete(heap, zero_index=False):
    if zero_index:
        heap.insert(0, None)

    print(f"Deleting root node from heap {heap}")

    if len(heap) == 1:
        print("Heap is empty")
        return

    root_val = heap[1]
    print(f"Root node is {root_val}")
    heap[1] = heap.pop()
    print(f"Swapped root node with last node in heap. New heap looks like this:")
    array_as_tree(heap)
    heapify_node(heap, 1)

    return root_val


arr = [None, 60, 50, 25, 40, 10, 15, 18, 12, 20]
heap_delete(arr)
print(arr)