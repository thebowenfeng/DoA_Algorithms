from tree_utils import DELIMITER


def merge(arr1, arr2):
    print(f"Merging {arr1} and {arr2}")
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result += arr1[i:]
    result += arr2[j:]
    return result


def mergesort(arr):
    print(DELIMITER)
    print(f"Performing mergesort on {arr}")

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    print(f"Split array into {arr[:mid]} and {arr[mid:]}")

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    result = merge(left, right)
    print(f"Merged two sub arrays into {result}")
    print(DELIMITER)

    return result
