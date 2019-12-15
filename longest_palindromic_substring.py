from collections import deque
# https://leetcode.com/problems/longest-palindromic-substring/discuss/121496/Python-DP-solution
class Solution(object):
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

    def lps(self, s):
        

        st = ''
        for i in range(len(s)):
            st += '#'+ s[i]
        st = '$'+st+'#%'
        
        P = [0]*len(st)
        C,R = 0, 0
        for i in range(1, len(st)-1):
            mirr = 2*C - i
            
            # update already expanded palindrome
            if i < R:
                P[i] = min(R-i, P[mirr])
            
            while st[i+(1+P[i])] == st[i-(1+P[i])]:
                P[i] += 1
            
            if i+P[i] > R:
                C = i
                R = i + P[i]
        
        # extract the longest palindromic substring from P, st
        length = max(P)
        index = P.index(length)
        string = st[index-length:index+length]
        return string.replace('#','')

abc = Solution()
print (abc.lps("abb"))