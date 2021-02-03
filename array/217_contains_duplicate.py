from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


print(contains_duplicate([2, 7, 11, 15]))
