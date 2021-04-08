"""
230. Kth Smallest Element in a BST
Medium

3595

83

Add to List

Share
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recursive_solution(self, root: TreeNode, k: int) -> int:
        def inorder(root: TreeNode) -> List[int]:
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
#             if not root:
#                 return

#             inorder(root.left, k, res)
#             res.append(root.val)
#             inorder(root.right, k, res)
        
        # res = []
        # inorder(root, k, res)
        # return res[k-1]
        return inorder(root)[k-1]
    
    def iterative_solution(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1
            if not k:
                return root.val
            root = root.right

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.iterative_solution(root, k)
        #return self.recursive_solution(root, k)