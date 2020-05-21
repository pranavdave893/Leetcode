class Solution(object):
    def nextPermutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        while nums[j] <= nums[i-1]:
            j-= 1
        
        nums[j], nums[i-1] = nums[i-1], nums[j]

        l = i
        r = len(nums) - 1

        # import pdb; pdb.set_trace()
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1; r-= 1
        
        return nums
        
        

abc = Solution()
print (abc.nextPermutation([1,1,5,1]))
# print (abc.nextPermutation([1,2,3]))
# print (abc.nextPermutation([3,2,1]))
# print (abc.nextPermutation([1,1,5]))
# print (abc.nextPermutation([5,3,4,2,1]))
        

