"""
Q: https://leetcode.com/problems/shortest-palindrome/
A: https://leetcode.com/problems/shortest-palindrome/discuss/60191/Share-my-easy-AC-python-solution-(without-fancy-algorithm)
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s2 = s[::-1]
        n = len(s)
        final_index = 0
        for i in range(n):
            if s[:n-i] == s2[i:]:
                final_index = i
                break

        return s2[:final_index]+s

abc = Solution()
abc.shortestPalindrome("aacecaaa")