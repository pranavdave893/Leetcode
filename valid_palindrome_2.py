class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        count = 0
        def get_result(l,r,s,count,forward=True):
            while l < r:
                if s[l] == s[r]:
                    l += 1; r -= 1
                elif count < 1:
                    if not forward:
                        r -=1
                    else:
                        l += 1
                    count += 1 
                else:
                    return False

            return True
        
        result1 = get_result(l,r,s, count)
        result2 = get_result(l,r,s,count,forward=False)
        
        return result1 or result2

abc = Solution()
print (abc.validPalindrome("abca"))
