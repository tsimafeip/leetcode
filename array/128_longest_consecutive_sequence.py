"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
Hard

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109
 
Follow up: Could you implement the O(n) solution?
"""

from typing import List


class Solution:

    def sort_solution(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        cur_seq, max_seq = 1, 1
        for i, num in enumerate(nums):
            if i == 0:
                continue

            if num == nums[i - 1] + 1:
                cur_seq += 1
                max_seq = max(max_seq, cur_seq)
            # we keep cur_seq active for the equal numbers
            elif num != nums[i - 1]:
                cur_seq = 1

        return max_seq

    def set_solution(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0

        for num in nums:
            if num - 1 not in nums_set:
                cur_num = num
                cur_seq = 1

                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_seq += 1

                max_seq = max(max_seq, cur_seq)
        return max_seq

    def longestConsecutive(self, nums: List[int]) -> int:
        # return self.sort_solution(nums)
        return self.set_solution(nums)


sol = Solution()
print(sol.numIslands(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(sol.numIslands(nums=[100, 4, 200, 1, 3, 2]))
