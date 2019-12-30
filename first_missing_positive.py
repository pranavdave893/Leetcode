class Solution(object):
    def firstMissingPositive(self, nums):

        if not nums:
            return 1

        start = 0
        end = len(nums)-1

        while start <= end:
            if nums[start] > len(nums):
                nums[start] = -nums[start]
                start += 1
                continue
            elif nums[start] > 0:
                replace = nums[start]-1
                if nums[start] == nums[replace]:
                    start+=1
                    continue
                nums[start], nums[replace] = nums[replace], nums[start]
            else:
                start += 1
        
        for x in range(len(nums)):
            if nums[x] != (x + 1):
                return x+1
        
        return nums[x]+1

abc = Solution()
print (abc.firstMissingPositive([1]))
# print  (abc.firstMissingPositive([1,2,0]))
# print  (abc.firstMissingPositive([3,4,-1,1]))
# print (abc.firstMissingPositive([7,8,9,11,12]))

