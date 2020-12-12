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


    def maxSlidingWindow_dq(self, nums, k):
        from collections import deque
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        result = []
        
        for i in range(len(nums)):
            # the first/left (max) element is out of the current window
            if q and i - q[0] == k:
                q.popleft()
            
            while q:
                # pop useles elements from last/right of the queue
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break
            
            q.append(i)
            
            if i >= k-1: # i == k-1 is the beginning of a full window
                result.append(nums[q[0]])
            
        return result

abc = Solution()
print (abc.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4))
print (abc.maxSlidingWindow_dq([1,2,3,4,5,6,7,8], 3))            