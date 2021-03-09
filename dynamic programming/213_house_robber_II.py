"""
213. House Robber II
Medium
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [0]
Output: 0
 

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        #everything except last house
        house1 = [0 for _ in range(len(nums))]
        
        house1[0] = nums[0]
        house1[1] = max(nums[1], house1[0])
        
        #everything except 1st house
        house2 = [0 for _ in range(len(nums))]
        house2[0] = 0
        house2[1] = nums[1]
        
        for i in range(2, len(nums)):
            house1[i] = max(house1[i-1], house1[i-2] + nums[i])
            house2[i] = max(house2[i-1], house2[i-2] + nums[i])  
        
        return max(house1[-2], house2[-1])