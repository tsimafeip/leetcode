from typing import List


def max_subarray(nums: List[int]) -> int:
    max_sum = max(nums)
    temp_sum = 0
    for num in nums:
        temp_sum = max(0, temp_sum)
        temp_sum += num
        max_sum = max(temp_sum, max_sum)
    return max_sum


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([1]))
print(max_subarray([0]))
print(max_subarray([-1]))
print(max_subarray([-100000]))
