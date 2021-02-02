from typing import List


def find_pivot_index(self, nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < nums[high]:
            high = mid
        else:
            low = mid + 1
    return low


def search(self, nums: List[int], target: int) -> int:
    pivot_index = self.find_pivot_index(nums)
    if target > nums[-1]:
        low, high = 0, pivot_index - 1
    else:
        low, high = pivot_index, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1
