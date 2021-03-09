"""
198. House Robber
Medium
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
             
Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 400
"""
class Solution:
    def house_arr_solution(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        #house = [0 for _ in range(len(nums))]
        house_0 = nums[0]
        house_1 = max(house_0, nums[1])
        cur_house = house_1
        
        for i in range(2, len(nums)):
            cur_house = max(house_1, house_0 + nums[i])
            house_0, house_1 = house_1, cur_house
        return cur_house
    
    def my_initial_solution(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        n0 = nums[0]
        n1 = nums[1]
        n2 = nums[0] + nums[2]
        cur_n = n2
                
        for i in range(3, len(nums)):
            cur_n = max(n0, n1) + nums[i]
            n0 = n1
            n1 = n2
            n2 = cur_n
        
        return max(n1, cur_n)
    
    def rob(self, nums: List[int]) -> int:
        return self.house_arr_solution(nums)