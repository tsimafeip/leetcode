"""
295. Find Median from Data Stream
Hard
https://leetcode.com/problems/find-median-from-data-stream/

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:
If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap_for_small_numbers = []
        self.min_heap_for_large_numbers = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap_for_small_numbers, -1*num)
        max_el = -1 * heapq.heappop(self.max_heap_for_small_numbers)
        heapq.heappush(self.min_heap_for_large_numbers, max_el)
        
        # only heap for small numbers can be larger
        if len(self.min_heap_for_large_numbers) > len(self.max_heap_for_small_numbers):
            min_el = heapq.heappop(self.min_heap_for_large_numbers)
            heapq.heappush(self.max_heap_for_small_numbers, -1* min_el)
            
        

    def findMedian(self) -> float:
        if not self.min_heap_for_large_numbers and not self.max_heap_for_small_numbers:
            return
        
        res = 0
        if len(self.min_heap_for_large_numbers) == len(self.max_heap_for_small_numbers):
            res = (self.min_heap_for_large_numbers[0] + -1*self.max_heap_for_small_numbers[0])*0.5
        else:
            res = -1*self.max_heap_for_small_numbers[0]
        
        return res


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()