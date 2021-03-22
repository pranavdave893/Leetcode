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

    def firstMissingPositive_CycleSort(self, nums):
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1
            # put num[i] to the correct place if nums[i] in the range [1, n]
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # so far, all the integers that could find their own correct place 
        # have been put to the correct place, next thing is to find out the
        # place that occupied wrongly
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

abc = Solution()
# print (abc.firstMissingPositive([1]))
# print  (abc.firstMissingPositive([1,2,0]))
print  (abc.firstMissingPositive_CycleSort([3,4,-1,1]))
# print (abc.firstMissingPositive([7,8,9,11,12]))

