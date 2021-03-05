"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
Easy

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def initialSolution(self, head: ListNode, val: int) -> ListNode:       
        while head and head.val == val:
            head = head.next
        
        root = head
        while head:
            while head.next and head.next.val == val:
                head.next = head.next.next
            head = head.next
        
        return root
        
    def refactoredSolution(self, head: ListNode, val: int) -> ListNode:
        before_root = ListNode(next=head)
        prev_node = before_root
        
        while head:
            if head.val == val:
                prev_node.next = head.next
            else:
                prev_node = head
            head = head.next
        return before_root.next
        
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        return self.initialSolution(head, val)
        #return self.refactoredSolution(head, val)