class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        start, end = 0, 0
        
        seen = set()
        
        ans = 0
        
        while end < len(s):
            
            if s[end] not in seen:
                seen.add(s[end])
                ans = max(ans, (end-start)+1)
                end += 1
            else:
                while s[end] in seen:
                    seen.remove(s[start])
                    start += 1
        
        return ans

abc = Solution()
print (abc.lengthOfLongestSubstring(" "))
                