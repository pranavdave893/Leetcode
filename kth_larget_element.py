from heapq import heappush, heappop, heapify, heappushpop
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        
        for x in nums:
            heappush(heap, -x)
        
        for _ in range(k):
            ans = heappop(heap)
        
        return abs(ans)
    
    
    def findKthLargest2(self, nums, k):
        min_heap = nums[:k]
        heapify(min_heap)

        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappushpop(min_heap, nums[i])
        
        return min_heap[0]
    
    
    def findKthLargest3(self, nums, k):
        return self.quickSelect(nums, 0, len(nums)-1, k)

    
    def quickSelect(self, nums, start, n, k): # quick select
        pos = self.partition(nums, start, n)
        if pos == k-1:
            return nums[pos]
        elif pos >= k:
            return self.quickSelect(nums, start, pos - 1, k)
        return self.quickSelect(nums, pos + 1, n, k)
        

    def partition(self, nums, left, right):
        pivot = nums[right] # pick the last one as pivot
        i = left
        for j in xrange(left, right): # left to right -1
            if nums[j] > pivot: # the larger elements are in left side
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right] # swap the i and the last element
        return i


abc = Solution()
# print (abc.findKthLargest([3,2,1,5,6,4], 2))
print (abc.findKthLargest3([3,2,1,5,6,4], 4))