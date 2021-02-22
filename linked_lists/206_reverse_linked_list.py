"""
206. Reverse Linked List
Easy
https://leetcode.com/problems/reverse-linked-list/  


Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        return self.recursive(head)
    
    def iterative(self, head: ListNode) -> ListNode:
        if head is None:
            return
        
        prev_node, cur_node = None, head
        while cur_node:
            cur_node.next, prev_node, cur_node = prev_node, cur_node, cur_node.next
        return prev_node
    
    def recursive(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: 
            return head
        p = self.recursive(head.next)
        head.next.next = head
        head.next = None
        return p