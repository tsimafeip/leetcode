def rotated_min_search(nums):
    if len(nums) == 1:
        return nums[0]

    if nums[0] < nums[-1]:
        return nums[0]

    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < nums[high]:
            high = mid
        else:
            low = mid + 1
    return nums[low]


print(rotated_min_search([1, 2, 3, 4, 5, 7, 8]))
