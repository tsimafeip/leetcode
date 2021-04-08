"""
94. Binary Tree Inorder Traversal
Medium
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]
 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up:
Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def iterativeInorderTraversal(self, root: TreeNode, res: List[int]):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left

            if len(stack) == 0:
                break

            root = stack.pop()
            res.append(root.val)
            root = root.right
                
    def recursiveInorderTraversal(self, root: TreeNode, res: List[int]):
        if not root:
            return
        self.recursiveInorderTraversal(root.left, res)
        res.append(root.val)
        self.recursiveInorderTraversal(root.right, res)
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        #self.recursiveInorderTraversal(root, res)
        self.iterativeInorderTraversal(root, res)
        return res