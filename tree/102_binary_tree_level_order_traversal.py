"""
102. Binary Tree Level Order Traversal
Medium
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        level_dict = defaultdict(list)
        
        queue = deque()
        queue.append((root, 0))
        
        while queue:
            cur_node, level = queue.popleft()
            level_dict[level].append(cur_node.val)
            for neighbour in [cur_node.left, cur_node.right]:
                if neighbour:
                    queue.append((neighbour, level+1))
        return list(level_dict.values())