class Solution(object):
    def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            unsorted = len(nums)
            for i in nums:
                index = nums.index(i)
                if i in nums[index:] and index != len(nums)-1:
                    nums.remove(i)
            return nums

abcd = Solution()
print abcd.removeDuplicates([1,1,2])
