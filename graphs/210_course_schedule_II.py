"""
210. Course Schedule II
Medium
https://leetcode.com/problems/course-schedule-ii/


There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.
Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_dict = defaultdict(list)
        for course_a, course_b in prerequisites:
            adj_dict[course_a].append(course_b)
        
        visited_nodes = set()
        course_path_set = set()
        course_path = []
        def dfs(cur_node: int) -> bool:
            if cur_node in visited_nodes:
                return False
        
            if cur_node in course_path_set:
                return True
            
            visited_nodes.add(cur_node)
            for neighbour_node in adj_dict[cur_node]:
                if not dfs(neighbour_node):
                    return False
            visited_nodes.remove(cur_node)
            
            course_path.append(cur_node)
            course_path_set.add(cur_node)
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return course_path
        
        
        
        
        
        
        
        
        