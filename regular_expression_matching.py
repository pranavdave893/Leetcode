class Solution(object):
    def isMatch_recur(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch_recur(text, pattern[2:]) or
                    first_match and self.isMatch_recur(text[1:], pattern))
        else:
            return first_match and self.isMatch_recur(text[1:], pattern[1:])
    
    def isMatch_recur_dp(self, s, p):
        lens = len(s) + 1
        lenp = len(p) + 1

        dp = [[False] * lenp for _ in range(lens)]
        dp[0][0] = True

        for j in range(1, lenp):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, lens):
            for j in range(1, lenp):
                
                if p[j-1] in {s[i-1], "."}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-2] in {s[i-1], "."})
        
        return dp[-1][-1]

    def test_1(self):
        s = "ab"
        p = ".*"
        assert True == self.isMatch_recur(s, p), "test_1"
        assert True == self.isMatch_recur_dp(s, p), "test_1"
    
    def test_2(self):
        s = "aab"
        p = "c*a*b"
        assert True == self.isMatch_recur(s, p), "test_2"
        assert True == self.isMatch_recur_dp(s, p), "test_2"
    
    def test_3(self):
        s = "mississippi"
        p = "mis*is*p*."
        assert False == self.isMatch_recur(s, p), "test_3"
        assert False == self.isMatch_recur_dp(s, p), "test_3"
    
    def test_4(self):
        s = "aaab"
        p = "a*b"
        try:
            assert True == self.isMatch_recur(s, p), "test_4"
            assert True == self.isMatch_recur_dp(s, p), "test_4"
        except Exception as ex :
            print (ex.message)
    
    def test_5(self):
        s = "aa"
        p = "a"
        assert False == self.isMatch_recur(s, p), "test_5"
        assert False == self.isMatch_recur_dp(s, p), "test_5"
    
    def test_6(self):
        s = "abcdef"
        p = ""
        assert False == self.isMatch_recur(s, p), "test_6"
        assert False == self.isMatch_recur_dp(s, p), "test_6"
    
    def test_7(self):
        s = "aaa"
        p = "ab*a*c*a"
        assert True == self.isMatch_recur(s, p), "test_6"
        assert True == self.isMatch_recur_dp(s, p), "test_6"
    

abc = Solution()
abc.test_1()
abc.test_2()
abc.test_3()
abc.test_4()
abc.test_5()
abc.test_6()
abc.test_7()


# if p == ".*":
        #     return True
        
        # if not s or not p:
        #     return False
        
        # x = len(s) - 1
        # y = len(p) - 1

        # while y >= 0:
        #     if x >=0 and (p[y] == "." or p[y] == s[x]):
        #         x -= 1
        #         y -= 1
            
        #     elif p[y] == "*" and y > 0:
        #         y -= 1
        #         char = p[y]

        #         while x >=0 and s[x] == char:
        #             x -= 1
                
        #         y -= 1
            
        #     elif x >=0 and p[y] != s[x]:
        #         return False
        #     else:
        #         return False
        
        # if x>=0 and y < 0:
        #     return False
        # else:
        #     return True
