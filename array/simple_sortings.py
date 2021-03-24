from typing import List


def selection_sort(nums: List[int]):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


def bubble_sort(nums):
    for i in reversed(range(len(nums))):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def insertion_sort(nums: List[int]):
    for i in range(1, len(nums)):
        key = nums[i]

        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


arr = [6, 3, 5, 1, 4, 2, 5]
insertion_sort(arr)
print(arr)
arr = [3, 5, 1, 4, 2]
selection_sort(arr)
print(arr)
arr = [3, 5, 1, 4, 2]
bubble_sort(arr)
print(arr)
