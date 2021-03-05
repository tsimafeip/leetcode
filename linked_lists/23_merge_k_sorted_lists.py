"""
23. Merge k Sorted Lists
Hard


You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nlogn_sorting_solution(self, lists: List[ListNode]) -> ListNode:
        values = []
        
        for head in lists:
            while head:
                values.append(head.val)
                head = head.next
        
        values.sort()
        before_root = ListNode()
        prev_node = before_root
        for value in values:
            cur_node = ListNode(value)
            prev_node.next = cur_node
            prev_node = cur_node
            
        return before_root.next
                
                
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.nlogn_sorting_solution(lists)