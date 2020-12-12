from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # XXX: This is with duplicate
        # l, r = 0, len(nums)-1

        # while l < r:
            
        #     m = l + (r-l)//2

        #     if nums[m] <nums[r]:
        #         r = m

        #     elif nums[m] > nums[l]:
        #         l = m+1
        #     else:
        #         r -= 1

        # Without duplicate

        l, r = 0, len(nums)-1

        while l < r:
            
            m = l + (r-l)//2

            if nums[m] <nums[r]:
                r = m

            elif nums[m] > nums[r]:
                l = m + 1
            
            else:
                r -= 1
        
        return nums[l]

        

abc = Solution()
# print (abc.findMin([1,3,5]))
# print (abc.findMin([2,2,2,0,1]))
# print (abc.findMin([3,3,1,3]))
print (abc.findMin([4,5,6,7,0,1,2]))
# print (abc.findMin([1,2]))