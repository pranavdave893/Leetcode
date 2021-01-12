class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        
        if not nums or len(nums) < 3:
            return answer
        
        nums.sort()
        n = len(nums)
        
        for x in range(n):
            if x>0 and nums[x] == nums[x-1]:
                continue
            
            if nums[x] > 0:
                break
            
            target = -nums[x]
            
            l = x + 1
            r = n - 1
            
            while (l < r):
                tmp = nums[l] + nums[r]
                
                if tmp == target:
                    answer.append([nums[x], nums[l], nums[r]])
                
                    l+=1
                    r-=1
                    
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while r>l and nums[r] == nums[r+1]:
                        r -= 1
                
                elif tmp > target:
                    r -= 1
                else:
                    l += 1
            
        return answer

abc = Solution()
print (abc.threeSum([-1,0,1,2,-1,-4]))