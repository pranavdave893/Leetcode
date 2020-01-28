class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0
        
        if s == s[::-1]:
            return 1
        
        ans = 0

        j = len(s)
        i = 0

        is_reverse = False
        while i < len(s) and j >= 0 and i!= j:
            substr = s[i:j]
            substr_2 = s[i+1:j]
            if substr == substr[::-1]:
                ans += 1
                if is_reverse:
                    j -= 1
                else:
                    i = j
                    j += 1
            
            elif substr_2 == substr_2[::-1]:
                ans += 1
                j = i + 1
                is_reverse = True
                
            
            else:
                j -= 1
        
        return ans

abc = Solution()
print (abc.removePalindromeSub("abb"))
print (abc.removePalindromeSub("baabb"))
print (abc.removePalindromeSub("ababa"))





