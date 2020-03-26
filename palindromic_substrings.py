class Solution(object):
    def countSubstrings(self, s):
        if not s: return 0
        ct = 0

        for i in xrange(len(s)):
            if s[:i+1] == s[:i+1][::-1]: ct +=1
        
        ct += self.countSubstrings(s[1:])
        return ct

    def countSubstrings2(self, s):
        count = 0
        
        # odd length palindrome
        for i in range(len(s)):
            count += self.helper(s, i, i)
        
        # even length palindrome
        for i in range(len(s)):
            count += self.helper(s, i, i+1)
        return count

    def helper(self, s, r, l):
        count = 0
        while r >= 0 and l < len(s):
            if s[r] == s[l]:
                count += 1
                r -= 1; l += 1
            else: break
        return count
    
    def countSubstrings_dp(self, s):
        self.cache = {}
        return self.memo(0, len(s)-1, s)

    def memo(self, l, r, s):
        if (l, r) in self.cache:
            return 0
        
        if l > r: return 0

        if s[l:r+1] == s[l:r+1][::-1]:
            self.cache[(l, r)] = 1 + self.memo(l+1, r, s) + self.memo(l, r-1, s)
        else:
            self.cache[(l, r)] = self.memo(l+1, r, s) + self.memo(l, r-1, s)
        
        return self.cache[(l, r)]
        



x = Solution()
print (x.countSubstrings2("aaaaaa"))
