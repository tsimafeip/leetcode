"""
347. Top K Frequent Elements
Medium
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""
class Solution:
    def counter_solution(self, nums: List[int], k: int) -> List[int]:
        return [k for k, v in Counter(nums).most_common(k)]
    
    def bucket_sort_solution(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        for num, num_count in Counter(nums).items():
            buckets[num_count].append(num)
        
        flat_nums = [val for bucket in buckets for val in bucket]
        return flat_nums[::-1][:k]
    
    def heap_solution(self, nums: List[int], k: int) -> List[int]:
        # to save N*logK complexity if n == k
        if k == len(nums):
            return nums
        
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num]+=1
         
        return heapq.nlargest(k, nums_dict.keys(), key=nums_dict.get)
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.bucket_sort_solution(nums, k)
        #return self.heap_solution(nums, k)