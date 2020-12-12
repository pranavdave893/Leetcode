from collections import deque
# https://leetcode.com/problems/longest-palindromic-substring/discuss/121496/Python-DP-solution
class Solution(object):
    def lps_simple(self, s):
        res = ""
        for i in range(len(s)):
            tmp = self.helpers(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            
            tmp = self.helpers(s, i, i+1)
            
            if len(tmp) > len(res):
                res = tmp
        
        return res
    
    
    def helpers(self, s, l, r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l -= 1 
            r += 1
        return s[l+1:r]


    def longestPalindrome_dp(self,s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = ""
        max_length = 1

        for i in range(n):
            dp[i][i] = True
            ans = s[i]
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = s[i:i+2]
                max_length = 2

        for x in range(n):
            for y in range(0, n-1):
                if s[x] == s[y] and dp[x+1][y-1]:
                    dp[x][y] = True

                    if max_length < y - x + 1:
                        ans = s[x:y+1]
                        max_length = y - x + 1
        
        return ans

    def lps_top_down(self, s):
        def F(i, j, memo):
            if i > j:
                return 0
            if i == j:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == s[j]:
                memo[(i, j)] = F(i+1, j-1, memo) + 2
            else:
                memo[(i, j)] = max(F(i+1, j, memo), F(i, j-1, memo))

            return memo[(i, j)]

        n = len(s)
        return F(0, n-1, {})

abc = Solution()
print (abc.lps_top_down("babad"))
print (abc.longestPalindrome_dp("babad"))