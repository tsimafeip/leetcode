from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    res = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]

    R = 1
    for i in reversed(range(len(nums))):
        res[i] = res[i] * R
        R *= nums[i]

    return res


def product_except_self_non_optimized(nums: List[int]) -> List[int]:
    L = [1 for _ in range(len(nums))]
    R = [1 for _ in range(len(nums))]
    cur_product = 1
    for i, num in enumerate(nums):
        L[i] = cur_product
        cur_product *= num

    cur_product = 1
    for i, num in enumerate((reversed(nums))):
        R[len(nums) - i - 1] = cur_product
        cur_product *= num

    for i in range(len(nums)):
        nums[i] = L[i] * R[i]

    return nums


assert product_except_self_non_optimized([1, 2, 3, 4]) == product_except_self([1, 2, 3, 4])
assert product_except_self_non_optimized([4, 5, 1, 8, 2, 10, 6]) == product_except_self([4, 5, 1, 8, 2, 10, 6])
