class Solution(object):
    # Recursive Solution.
    def shortestPalindrome(self, s):
        if not s:
            return 0
        
        def makePalindrome(new_str, start, end):
            if start == end:
                return 0
            
            if new_str[start] == new_str[end-1]: 
                if new_str[start] == new_str[end]:
                    return 0
                else:
                    return 1
            
            else:
                if new_str[start] == new_str[end]:
                    return makePalindrome(new_str, start+1, end-1)

                x = makePalindrome(new_str, start+1, end)
                y = makePalindrome(new_str, start, end-1)
                return min(x, y) + 1

        return makePalindrome(s, 0, len(s)-1)

abc = Solution()
print (abc.shortestPalindrome('abcd'))
