class Solution(object):
    def distributeCandies(self, candies, n):
        
        ans = [0] * n
        
        start = 1
        i = 0
        
        while candies >= 0:
            if start > candies:
                ans[i] += candies
                break
            ans[i] += start
            candies -= start
            start += 1
            i += 1
            if i >= n:
                i= 0
        return ans

abc = Solution()
print (abc.distributeCandies(10,3))