
"""
Q: https://leetcode.com/discuss/interview-question/169334/Facebook-or-Phone-screen-or-Sorted-Iterator
tags : Facebook, medium
Time Complexity : O(N Log(K)) where N is total numbers and K is length of lists
Space complexity : O(K)
"""

from heapq import heappush, heappop
class Solution(object):

    def __init__(self, lists):
        self.lists = lists
        self.heap = []

        for i, x in enumerate(lists):
            if x:
                heappush(self.heap, (x[0], i, 0))
    

    def hasNext(self):
        return len(self.heap) > 0
    

    def Next(self):
        if not self.hasNext():
            return None
        
        heap = self.heap
        lists = self.lists
        
        val, list_idx, val_idx = heappop(heap)
        
        if val_idx + 1 < len(lists[list_idx]):
            heappush(heap, (lists[list_idx][val_idx+1], list_idx, val_idx+1))
        
        return val

s = Solution([[1, 4, 5, 8, 9], [3, 4, 4, 6], [0, 2, 8]])
while s.hasNext():
    print(s.Next())

