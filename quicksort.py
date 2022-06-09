from tree_utils import DELIMITER


def lomuto(arr):
    print("Performing lomuto partitioning on array:", arr)
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    ptr = 0

    print("Pivot is:", pivot, "Pointer is initialized at:", ptr)

    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            print(f"Current element {arr[i]} (index {i}) is smaller than pivot {pivot}. Swapping with element at index {ptr}. Pointer moved to {ptr + 1}")
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
            print(f"New array: {arr}")

    print("Swapping pivot with element at index", ptr)
    arr[-1], arr[ptr] = arr[ptr], arr[-1]
    print("New array looks like:",arr, "Pointer is now at:", ptr)
    return ptr


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    print(DELIMITER)
    print(f"Performing quicksort on array: {arr}")
    ind = lomuto(arr)

    first = arr[:ind]
    second = arr[ind + 1:]
    print(f"First partition: {first}. Second partition: {second}")

    result = quicksort(first) + [arr[ind]] + quicksort(second)
    print(f"Resulting array: {result}")
    print(DELIMITER)
    return result


print(quicksort([1, 7, 6, 2, 9, 4, 3, 5]))