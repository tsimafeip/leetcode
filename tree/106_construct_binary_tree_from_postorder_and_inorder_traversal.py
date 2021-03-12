"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: []

Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def construct_node(self, left_border: int, right_border: int) -> TreeNode:
        if left_border > right_border:
            return

        root_node = TreeNode(self.postorder[self.root_index_postorder])
        self.root_index_postorder -= 1
        if left_border != right_border:
            root_index_inorder = self.inorder_dict[root_node.val]
            root_node.right = self.construct_node(root_index_inorder + 1, right_border)
            root_node.left = self.construct_node(left_border, root_index_inorder - 1)
        return root_node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.root_index_postorder = len(postorder) - 1
        self.postorder = postorder
        self.inorder_dict = {node_val: index for index, node_val in enumerate(inorder)}
        return self.construct_node(0, len(inorder) - 1)


sol = Solution()
sol.buildTree([1, 2], [1, 2])
