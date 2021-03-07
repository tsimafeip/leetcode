"""
23. Merge k Sorted Lists
Hard
https://leetcode.com/problems/merge-k-sorted-lists/

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
from queue import PriorityQueue
from itertools import count

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
    
    def heap_solution(self, lists: List[ListNode]) -> ListNode:
        ListNode.__lt__ = lambda self, other_node : self.val < other_node.val
        lists = [l for l in lists if l]
        heapq.heapify(lists)
                
        dummy = prev_node = ListNode()
        while lists:
            cur_node = heapq.heappop(lists)
            prev_node.next = cur_node
            prev_node = cur_node
            if cur_node.next:
                heapq.heappush(lists, cur_node.next)
        return dummy.next
    
    def priority_queue_solution(self, lists: List[ListNode]) -> ListNode:
        queue = PriorityQueue()
        unique = count()
        
        for list_head in lists:
            if list_head:
                queue.put((list_head.val, next(unique), list_head))
                
        dummy = queue = ListNode()
        while not queue.empty():
            _, _, cur_node = queue.get()
            prev_node.next = cur_node
            prev_node = cur_node
            if cur_node.next:
                queue.put((cur_node.next.val, next(unique), cur_node.next))
        return dummy.next
    
    def divide_and_conquer(self, lists: List[ListNode]) -> ListNode:
    
        def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
            dummy = cur = ListNode()            
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
        
        n = len(lists)
        interval = 1
        
        while interval < n:
            for i in range(0, n - interval, interval*2):
                lists[i] = self.merge_two_lists(lists[i], lists[i+interval])
            interval*=2
        
        return lists[0] if lists else None
                
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.divide_and_conquer(lists)
        #return self.heap_solution(lists)
        #return self.nlogn_sorting_solution(lists)