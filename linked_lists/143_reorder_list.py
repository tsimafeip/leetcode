"""
143. Reorder List
Medium
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 
Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
        temp_node, prev_node, cur_node = None, None, head
        while cur_node:
            temp_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = temp_node
        return prev_node
    
    def merge(self, l1: ListNode, l2: ListNode) -> None:
    
        while l1 and l2:
            l1_next, l2_next = l1.next, l2.next
            
            l1.next = l2
            
            if not l1_next:
                break
            l2.next = l1_next
            
            l1 = l1_next
            l2 = l2_next
        
    
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: 
            return
        
        prevMiddle,slow, fast = [head]*3
        while fast and fast.next:
            prevMiddle = slow
            slow = slow.next
            fast = fast.next.next
        
        prevMiddle.next = None
        l2 = self.reverseList(slow)
        self.merge(head, l2)