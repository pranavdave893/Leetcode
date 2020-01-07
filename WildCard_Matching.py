class Solution(object):
    def isMatch(self, s, p):
        
        len_p = len(p)
        len_s = len(s)

        dp = [[0] * (len_p+1) for _ in range(len_s+1)]

        dp[0][0] = 1

        for x in range(1, len_p+1):
            if p[x-1] == '*':
                dp[0][x] = dp[0][x-1]
        
        for i in range(1, len_s+1):
            for j in range(1, len_p+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        
        return bool(dp[-1][-1])

abc = Solution()
# print (abc.isMatch("aa", "a"))
# print (abc.isMatch("aa", "*"))
# print (abc.isMatch("cb", "?a"))
# print (abc.isMatch("adceb", "*a*b"))
# print (abc.isMatch("acdcb", "a*c?b"))
print (abc.isMatch("ab", "?*"))
