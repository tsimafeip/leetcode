from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    arr = [1] * len(nums)

    for i in range(len(nums)):
        for j in reversed(range(i)):
            if nums[i] > nums[j]:
                arr[i] = max(arr[i], arr[j] + 1)

    return max(arr)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
