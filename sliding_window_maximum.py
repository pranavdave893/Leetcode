from heapq import *

class Solution(object):
    def get_max_value(self, heap, start):
            mx_idx = heap[0][1]
            mx_value = -heap[0][0]
            while start > mx_idx:
                heappop(heap)
                mx_idx = heap[0][1]
                mx_value = -heap[0][0]
            return mx_value

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        heap = []
        for i in range(k):
            heappush(heap, (-nums[i], i))
        
        start, end = 0, k-1

        ans = []

        while end < len(nums):
            print (heap, start)
            mx_value = self.get_max_value(heap, start)
            ans.append(mx_value)

            start += 1
            end += 1
            
            if end <= len(nums)-1:
                heappush(heap, (-nums[end], end))
        
        return ans


abc = Solution()
print (abc.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4))




            