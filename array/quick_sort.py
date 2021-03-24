# 1) Pick an element, called a pivot, from the array.
# 2) Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot,
# while all elements with values greater than the pivot come after it (equal values can go either way).
# After this partitioning, the pivot is in its final position. This is called the partition operation.
# 3) Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array
# of elements with greater values.
from typing import List
import numpy as np


def lomuto_partition(arr: List[int], low: int, high: int) -> int:
    # i is an index for the first element of B part (bigger or equal to the pivot).
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot or (arr[j] == pivot and i - low < j - i):
            arr[i], arr[j] = arr[j], arr[i]
            # move right border of the A part to the right.
            i += 1
    arr[high], arr[i] = arr[i], arr[high]
    return i


def lomuto_partition_r(arr: List[int], low: int, high: int) -> int:
    random_index = np.random.randint(low, high + 1)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return lomuto_partition(arr, low, high)


def hoare_partition(arr: List[int], low: int, high: int) -> int:
    # algorithm: move two pointers with respect to pivot conditions.
    # then swap elements and move pointers another one time.
    pivot = arr[np.random.randint(low, high + 1)]
    i = low - 1
    j = high + 1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr: List[int], low: int, high: int):
    if high > low:
        p = lomuto_partition_r(arr, low, high)
        quick_sort(arr, low, p - 1)
        #p = hoare_partition(arr, low, high)
        #quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)


def run_quick_sort(arr: List[int]):
    quick_sort(arr, 0, len(arr) - 1)


arr = list(np.random.randint(1, 15, 20))
# arr = [1, 3, 4, 2, 2, 5]
print(arr)
run_quick_sort(arr)
print(arr)
