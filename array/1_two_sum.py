from typing import List


def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
    for i, num in enumerate(nums[:-1]):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - num:
                return [i, j]


def two_sum_dict(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for i, num in enumerate(nums):
        complement_index = num_dict.get(target - num, None)
        if complement_index is not None:
            return [complement_index, i]
        num_dict[num] = i


print(two_sum_dict([2, 7, 11, 15], 9))
