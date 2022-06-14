from tree_utils import DELIMITER


def lomuto(arr):
    print("Performing lomuto partitioning on array:", arr)
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    ptr = 0

    print("Pivot is:", pivot, "Pointer is initialized at:", ptr)

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            ptr += 1
            print(f"Current element {arr[i]} (index {i}) is smaller than pivot {pivot}. Pointer moved to {ptr}. Swapping with element at index {ptr}")
            arr[i], arr[ptr] = arr[ptr], arr[i]
            print(f"New array: {arr}")

    print("Swapping pivot with element at index", ptr)
    arr[0], arr[ptr] = arr[ptr], arr[0]
    print("New array looks like:",arr, "Pointer is now at:", ptr)
    return ptr


def hoare(arr):
    print("Performing hoare partitioning on array:", arr)
    pivot = arr[0]
    i = 0
    j = len(arr)

    while (True):
        print(DELIMITER)
        # Find leftmost element greater than
        # or equal to pivot
        i += 1
        while (i < len(arr)) and (arr[i] < pivot):
            print(f"Element at index {i} is smaller than pivot {pivot}. Pointer moved to {i + 1}")
            i += 1

        if i >= len(arr):
            i = len(arr) - 1
            print(f"i exceeds array length. Pointer moved to {i}")
        else:
            print(f"Element at index {i} is greater than pivot {pivot}. Leftmost element greater than or equal to pivot is at index {i}")

        # Find rightmost element smaller than
        # or equal to pivot
        j -= 1
        while (j > 0) and (arr[j] > pivot):
            print(f"Element at index {j} is greater than pivot {pivot}. Pointer moved to {j - 1}")
            j -= 1

        if j <= 0:
            j = 0
            print(f"j is less than 0. Pointer moved to {j}")
        else:
            print(f"Element at index {j} is smaller than pivot {pivot}. Rightmost element smaller than or equal to pivot is at index {j}")

        print(f"Performing swap with elements at {i} and {j} on {arr}")
        arr[i], arr[j] = arr[j], arr[i]
        print(f"Result: {arr}")

        # If two pointers met.
        if (i >= j):
            print(f"Two pointers have met/crossed. Performing swap with elements at {i} and {j} on {arr}")
            arr[i], arr[j] = arr[j], arr[i]
            print(f"Result: {arr}")
            print(f"Swapping pivot with element at index {j}")
            arr[0], arr[j] = arr[j], arr[0]
            print(f"Final result: {arr}. Pivot at index {j}")
            return j


def quicksort(arr, partitioning_func: str):
    func = None
    if partitioning_func == "hoare":
        func = hoare
    elif partitioning_func == "lomuto":
        func = lomuto
    else:
        raise ValueError("Invalid partitioning function")

    if len(arr) <= 1:
        return arr

    print(DELIMITER)
    print(f"Performing quicksort on array: {arr}")
    ind = func(arr)

    first = arr[:ind]
    second = arr[ind + 1:]
    print(f"First partition: {first}. Second partition: {second}")

    result = quicksort(first, partitioning_func) + [arr[ind]] + quicksort(second, partitioning_func)
    print(f"Resulting array: {result}")
    print(DELIMITER)
    return result