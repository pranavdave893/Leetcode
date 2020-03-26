class Solution(object):
    def splitArray(self, nums, m):
        low, high = max(nums), sum(nums)

        while low < high:
            
            mid = low + (high-low) / 2
            n = 1
            curr = 0

            for x in nums:
                if curr + x > mid:
                    n += 1
                    curr = 0
                curr += x
            
            if n > m: low = mid+1
            else: high = mid
        
        return low



abc = Solution()
print (abc.splitArray([7,2,5,10,8], 2))