"""
200. Number of Islands
Medium
https://leetcode.com/problems/number-of-islands/

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nodes_to_visit_set = {(i, j) for i, row in enumerate(grid) for j, num in enumerate(row) if num == "1"}

        def bfs():
            queue = deque()
            queue.append(nodes_to_visit_set.pop())

            while queue:
                cur_node = queue.popleft()
                i, j = cur_node
                neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                for neighbour in neighbours:
                    if neighbour in nodes_to_visit_set:
                        queue.append(neighbour)
                        nodes_to_visit_set.remove(neighbour)
                        

        bfs_runs_count = 0
        while nodes_to_visit_set:
            bfs()
            bfs_runs_count += 1

        return bfs_runs_count


sol = Solution()
print(sol.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(sol.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
