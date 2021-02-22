"""
226. Invert Binary Tree
Easy
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        return self.recursive_solution(root)
    
    def iterative_solution(self, root: TreeNode) -> TreeNode:
        queue = deque()
        queue.append(root)
        while queue:
            cur_node = queue.popleft()
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            if cur_node.left: queue.append(cur_node.left)
            if cur_node.right: queue.append(cur_node.right)
        return root
    
    def recursive_solution(self, root: TreeNode) -> TreeNode:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root