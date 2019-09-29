class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # nums.sort()
        # max_sum = 0
        # i = 0
        # while (i<= len(nums)-1):
        #     max_sum += nums[i]
        #     i += 2
        
        # return max_sum
        res = [0]*20001
        for i in nums:
            res[i+10000]+=1
        total, flag=0, 0
        for idx, freq in enumerate(res):
            if freq:
                import pdb; pdb.set_trace()
                freq-=flag
                calc, flag = divmod(freq,2)
                total+=(calc+flag)*(idx-10000)
        return total

abc = Solution()
print (abc.arrayPairSum([1,4,3,2,5,6]))