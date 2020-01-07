class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        reminder = 0
        ans = 0
        dct = {}
        sums = 0
        for x in A:
            if reminder in dct:
                dct[reminder] += 1
            else:
                dct[reminder] = 1
            
            sums+= x
            reminder = sums % K
            if reminder in dct:
                ans += dct.get(reminder)
        
        return ans

abc = Solution()
print (abc.subarraysDivByK([4,5,0,-2,-3,1], 5))