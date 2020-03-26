class Solution:
    def subarraySum(self, nums, k):
        dct = {}
        result = 0
        sums = 0

        for num in nums:
            if dct.get(sums,None):
                dct[sums] += 1
            else:
                dct[sums] = 1
            
            sums += num
            if (sums - k) in dct:
                result += dct[sums-k]

        return result 


        
# XXX : similar problem sub array sum divisible by k.
abc = Solution()
print (abc.subarraySum([1,2,0,3,0],3))