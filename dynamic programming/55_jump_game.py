"""
55. Jump Game
Medium
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index. 

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:
1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105
"""
class Solution:
    
    def greedy_solution(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        for i in reversed(range(0, len(nums))):
            if i + nums[i] >=last_index:
                last_index = i
        return last_index == 0
    
    def top_down(self, pos: int, nums: List[int], memo_arr: List[int]) -> bool:
        if memo_arr[pos] != -1:
            return memo_arr[pos]
        
        max_jump_len = min(pos + nums[pos], len(nums) - 1)
        
        for i in range(pos+1, max_jump_len + 1):
            if self.top_down(i, nums, memo_arr):
                memo_arr[pos] = 1
                return True
        
        memo_arr[pos] = 0
        return False
    
    def bottom_up(self, pos: int, nums: List[int], memo_arr: List[int]) -> bool:
        
        for i in reversed(range(0, len(nums)-1)):
            max_jump = min(len(nums) - 1, i + nums[i])
            for j in range(i+1, max_jump + 1):
                if memo_arr[j] == 1:
                    memo_arr[i] = 1
                    break
            
        return memo_arr[0] == 1

    
    def canJump(self, nums: List[int]) -> bool:
        #memo_arr = [-1]*len(nums)
        #memo_arr[-1] = 1
        #return self.top_down(0, nums, memo_arr)
        #return self.bottom_up(0, nums, memo_arr)
        return self.greedy_solution(nums)