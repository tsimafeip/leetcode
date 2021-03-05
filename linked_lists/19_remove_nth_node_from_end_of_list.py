"""
19. Remove Nth Node From End of List
Medium
https://leetcode.com/problems/remove-nth-node-from-end-of-list/


Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def base_two_pass_solution(self, head: ListNode, n: int) -> ListNode:        
        before_root = ListNode(next=head)
        nodes_count = 0
        
        while head:
            nodes_count+=1
            head = head.next
        
        counter = 0
        target = nodes_count - n + 1
        
        prev_node, head = before_root, before_root.next

        while head:
            counter+=1
            if counter == target:
                prev_node.next = head.next
                break
            else:
                prev_node = head
            head = head.next
        
        return before_root.next
            
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return self.base_two_pass_solution(head, n)