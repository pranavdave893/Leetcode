from collections import Counter

class Solution():
    def get_smallest_substr(self, s):

        if not s: return 0

        seen = set()

        start, end = 0, 0

        ans = float('max')

        while end < len(s):
            if s not in seen:
                seen.add(s[end])
                end += 1
            
            else:
                ans = min(ans, (end-start) + 1)
                while s[start] in seen:
                    seen.remove(s[start])
                    start += 1





