class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        start = (n/2)
        ans = []
        for i in range(-start, start+1):
            if n%2 ==0 and i == 0:
                continue
            ans.append(i)
        

        return ans
abc = Solution()
print (abc.sumZero(4))
print (abc.sumZero(5))
print (abc.sumZero(6))