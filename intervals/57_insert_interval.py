"""
57. Insert Interval
Medium
https://leetcode.com/problems/insert-interval/submissions/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
 

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105
"""
from typing import List

class Solution:
    
    def my_solution(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        free_index = 0
        res_left = res_right = insertion_index = None
        for i, (cur_left, cur_right) in enumerate(intervals):
            if newInterval[1] >= cur_left and newInterval[0] <= cur_right:
                if res_left == None:
                    res_left = min(newInterval[0], cur_left)
                    insertion_index = i
                res_right = max(newInterval[1], cur_right)
            else:
                # we are on the right side and insertion index is not set, then insert before the current interval
                if insertion_index is None and cur_left > newInterval[1]:
                    res_left, res_right = newInterval
                    insertion_index = i
                intervals[free_index] = [cur_left, cur_right]
                free_index+=1
        
        # all actual intervals are lower than the new interval, then append it to the end
        if insertion_index is None:
            intervals.append(newInterval)
        else:
            intervals.insert(insertion_index, [res_left, res_right])
        return intervals[:free_index+1]
        
    def sort_solution(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval, ]
            
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        
        i = 1
        free_index = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[free_index-1][1]:
                intervals[free_index-1][0] = min(intervals[free_index-1][0], intervals[i][0])
                intervals[free_index-1][1] = max(intervals[free_index-1][1], intervals[i][1])
            else:
                intervals[free_index] = intervals[i]
                free_index+=1
            i+=1
            
            
        return intervals[:free_index]
        
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:       
        return self.sort_solution(intervals, newInterval)
        #return self.my_solution(intervals, newInterval)

sol = Solution()
assert [[1,5],[6,9]] == sol.insert([[1,3],[6,9]], [2,5])
assert [[1,2],[3,10],[12,16]] == sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
assert [[5,7]] == sol.insert([], [5,7])
assert [[1,5]] == sol.insert([[1,5]], [2,3])
assert [[1,7]] == sol.insert([[1,5]], [2,7])
assert [[3,5],[6,6],[12,15]] == sol.insert([[3,5],[12,15]], [6,6])
assert [[1,5],[6,8]] == sol.insert([[1,5]], [6,8])
assert [[1,5],[6,8]] == sol.insert([[6,8]], [1,5])



















