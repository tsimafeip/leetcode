from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    def all_two_sums(nums: List[int], target: int, cur_index: int) -> List[List[int]]:
        valid_results = set()
        res = []
        seen = set()
        for index, num in enumerate(nums):
            if index == cur_index:
                continue
            complement = target - num
            if complement in seen and tuple([num, complement]) not in valid_results:
                valid_results.add(tuple([num, complement]))
                res.append([num, complement])
            else:
                seen.add(num)
        return res

    valid_results = set()
    result = []

    for index, num in enumerate(nums):
        target = 0 - num
        two_sum_results = all_two_sums(nums, target, index)
        if two_sum_results:
            for two_sum_res in two_sum_results:
                two_sum_res.append(num)
                res_array = sorted(two_sum_res)
                if tuple(res_array) not in valid_results:
                    valid_results.add(tuple(res_array))
                    result.append(res_array)
    return result


def fast_three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i, num in enumerate(nums[:-2]):
        # we skip equal numbers
        if i == 0 or nums[i] != nums[i - 1]:
            target = 0 - num
            low, high = i + 1, len(nums) - 1
            while low < high:
                if nums[low] + nums[high] == target:
                    result.append([nums[low], nums[i], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] > target:
                    high -= 1
                else:
                    low += 1
    return result


print(fast_three_sum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
