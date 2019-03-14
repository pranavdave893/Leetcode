class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        max_sum = 0
        i = 0
        while (i<= len(nums)-1):
            max_sum += nums[i]
            i += 2
        
        return max_sum

abc = Solution()
print (abc.arrayPairSum([1,4,3,2,5,6]))