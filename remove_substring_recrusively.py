"""
https://leetcode.com/discuss/interview-question/124919/Twitter-or-Remove-Substring-Recursively
Tags: recrusion, twitter
"""

class Solution():
    def recursive_remove(self, s, t):

        if t not in s:
            return 0

        t_len = len(t)
        start_point = []

        for i in range(len(s) - t_len + 1):
            if s[i : i + t_len] == t:
                start_point.append(i)
        
        res = 0

        for i in start_point:
            res = max(res, self.recursive_remove(s[:i] + s[i+t_len:], t) + 1)
        
        return res

abc = Solution()
print (abc.recursive_remove("abababaaba", "ababa"))
