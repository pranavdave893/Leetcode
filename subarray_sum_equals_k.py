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


        

abc = Solution()
print (abc.subarraySum([0,0,0,0,0,0,0,0,0,0],0))