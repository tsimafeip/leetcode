def max_product(nums):
    res = max(nums)
    cur_max, cur_min = 1, 1
    for num in nums:
        cur_max, cur_min = max(num, cur_max * num, cur_min * num), min(num, cur_max * num, cur_min * num)
        res = max(cur_max, res)
    return res


print(max_product([2, 3, -2, 4]))
