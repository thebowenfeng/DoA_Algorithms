from math import log
from tree_utils import DELIMITER


def radixsort(arr):
    print(f"Performing radixsort on {arr}")
    max_num = max(arr)
    print(f"Max number in the array is {max_num}. It has {len(str(max_num))} digits.")
    exp = 1
    while max_num // exp > 0:
        print(DELIMITER)
        print(f"Currently sorting on the {int(log(exp, 10) + 1)}th LSD (least significant digit, {int(log(exp, 10) + 1)}th digit from right to left)")
        bucket = [[] for _ in range(10)]
        for num in arr:
            bucket[(num // exp) % 10].append(num)
        arr = []
        for bucket_arr in bucket:
            arr += bucket_arr
        exp *= 10
        print(f"Bucket: {bucket}")
        print(f"Sorted array: {arr}")

    print(f"Final sorted array: {arr}")
    return arr
