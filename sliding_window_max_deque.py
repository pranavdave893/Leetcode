from collections import deque

class Solution(object):
    def add_to_dq(self, nums, dq, i):
        # Add index to dq.
        
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
    
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        
        ans = []
        dq = deque()
        for i in range(k):
            self.add_to_dq(nums, dq, i)
        
        start = 0
        end = k - 1

        while end < len(nums):
            while True:
                if dq[0] >= start:
                    ans.append(nums[dq[0]])
                    break
                else:
                    dq.popleft()
            
            start += 1
            end += 1

            if end < len(nums):
                self.add_to_dq(nums, dq, end)
        
        return ans

abc = Solution()
print (abc.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4))
# print (abc.maxSlidingWindow([-1,1], 1))
                
                    

        