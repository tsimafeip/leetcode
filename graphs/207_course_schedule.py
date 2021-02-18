"""
207. Course Schedule
Medium
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_dict = defaultdict(list)
        for course_a, course_b in prerequisites:
            adj_dict[course_a].append(course_b)
        
        visited_nodes = set()
        def dfs(cur_node: int) -> bool:
            if cur_node in visited_nodes:
                return False
        
            if not adj_dict[cur_node]:
                return True
            
            visited_nodes.add(cur_node)
            for neighbour_node in adj_dict[cur_node]:
                if not dfs(neighbour_node):
                    return False
            visited_nodes.remove(cur_node)
            
            # we clean prerequisites for current course, since they are reachable, no need to solve the task again
            adj_dict[cur_node] = []
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        
        
        
        
        
        
        
        
        