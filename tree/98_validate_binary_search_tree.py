"""
98. Validate Binary Search Tree
Medium
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check_bst(self, root: TreeNode, low: float, high: float) -> bool:
        if not root:
            return True
        
        if not (root.val > low and root.val < high):
            return False
        
        return self.check_bst(root.left, low, root.val) and self.check_bst(root.right, root.val, high)
        
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_bst(root, float('-inf'), float('inf'))
            
        
            
        
        
        
        
        
    