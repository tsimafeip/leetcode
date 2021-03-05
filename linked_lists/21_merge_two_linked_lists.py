"""
21. Merge Two Sorted Lists
Easy
https://leetcode.com/problems/merge-two-sorted-lists/


Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def firstSolution(self, l1: ListNode, l2: ListNode) -> ListNode:
        root_node, prev_node, cur_node = [None]*3
        while l1 and l2:
            prev_node = cur_node
            if l1.val < l2.val:
                cur_node = ListNode(l1.val)
                l1 = l1.next
            else:
                cur_node = ListNode(l2.val)
                l2 = l2.next
            
            if prev_node:
                prev_node.next = cur_node
            else:
                # first element
                root_node = cur_node
        
        active_list = l1 if l1 else l2
        if active_list is not None:
            if cur_node:
                cur_node.next = active_list
            else:
                return active_list
        
        return root_node
    
     def refactoredSolution(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return dummy.next
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.refactoredSolution(l1, l2)