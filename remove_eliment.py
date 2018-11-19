class Solution(object):
    def removeElement(self, nums, val):
        count = nums.count(val)
        for i in range(count):  
            if val in nums:
                remove val

abc = Solution()
abc.removeElement([3,2,2,3],3)