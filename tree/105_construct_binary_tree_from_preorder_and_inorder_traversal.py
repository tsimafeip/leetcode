"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
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

        root_node = TreeNode(self.preorder[self.root_index_preorder])
        self.root_index_preorder += 1
        if left_border != right_border:
            root_index_inorder = self.inorder_dict[root_node.val]
            root_node.left = self.construct_node(left_border, root_index_inorder - 1)
            root_node.right = self.construct_node(root_index_inorder + 1, right_border)
        return root_node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.root_index_preorder = 0
        self.preorder = preorder
        self.inorder_dict = {node_val: index for index, node_val in enumerate(inorder)}
        return self.construct_node(0, len(inorder) - 1)


sol = Solution()
sol.buildTree([1, 2], [1, 2])
