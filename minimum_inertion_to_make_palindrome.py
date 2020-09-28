"""
Recursion : https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/discuss/723879/top-down-approch-dynamic-programming-with-explanation
"""
class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return 0
        
        def makePalindrome_recursion(new_str, start, end):
            if start == end:
                return 0
            
            if start == end-1: 
                if new_str[start] == new_str[end]:
                    return 0
                else:
                    return 1
            
            
            if new_str[start] == new_str[end]:
                return makePalindrome_recursion(new_str, start+1, end-1)

            x = makePalindrome_recursion(new_str, start+1, end)
            y = makePalindrome_recursion(new_str, start, end-1)
            return min(x, y) + 1

        print makePalindrome_recursion(s, 0, len(s)-1)


        def makePalindrome_dp(new_str, n):
            """
            n = length of string
            """
            dp_matrix = [[0]*len(new_str) for i in range(n)]

            for x in range(1, n):
                l = 0
                for y in range(x, n):
                    if new_str[l] == new_str[y]:
                        dp_matrix[l][y] = dp_matrix[l+1][y-1]
                    else:
                        dp_matrix[l][y] = min(dp_matrix[l+1][y], dp_matrix[l][y-1]) + 1

                    l += 1
            
            last_max_count = max(dp_matrix[l+1][y], dp_matrix[l][y-1]) + 1
            last_min_count = dp_matrix[0][n-1]
            
            last_min_count_str = new_str[-last_min_count:][::-1] + new_str
            if last_min_count_str == last_min_count_str[::-1]: return last_min_count_str
           
            last_max_count_str = new_str[-last_max_count:][::-1] + new_str
            if last_max_count_str == last_max_count_str[::-1]: return last_max_count_str
        
        print makePalindrome_dp(s, len(s))

abc = Solution()
abc.shortestPalindrome("abb")
