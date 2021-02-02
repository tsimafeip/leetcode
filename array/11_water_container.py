from typing import List


def maxArea(height: List[int]) -> int:
    cur_max, low, high = 0, 0, len(height) - 1
    get_max = lambda: min(height[low], height[high]) * (high - low)
    while low < high:
        cur_max = max(cur_max, get_max())
        if height[low] < height[high]:
            low += 1
        else:
            high -= 1

    return cur_max


# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# print(maxArea([1, 1]))
# print(maxArea([4, 3, 2, 1, 4]))
# print(maxArea([1, 2, 1]))
# print(maxArea([1, 2, 4, 3]))
# print(maxArea([1, 8, 6, 2, 5, 4, 8, 25, 7]))
print(maxArea([1, 8, 100, 2, 100, 4, 8, 3, 7]))
print(maxArea([1, 3, 2, 1]))
