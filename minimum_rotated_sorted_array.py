class Solution(object):
    def findMin(self, target, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        high = len(nums) - 1
        if nums[lo] == target:
            return lo
        
        if nums[high] == target:
            return high

        while lo < high:
            
            mid = (lo + high) / 2

            if nums[mid] > nums[high]:
                lo = mid +1
            else:
                high = mid
        
        return nums[lo]



abc = Solution()
print (abc.findMin([3,4,5,6,7,8,9,10,2]))
print (abc.findMin([4,0,1,2,3]))