class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        dct = {}
        len_1 = 0
        len_2 = 0

        i, j = 0, 0

        while j < len(s):
            if s[j] not in dct:
                dct[s[j]] = 1
                len_1 += 1
                j += 1
                if len_1 >= len_2:
                    len_2 = len_1
            else:
                while s[j] in dct:
                    del dct[s[i]]
                    i += 1
                    len_1 -= 1
                
        
        return max(len_1, len_2)

abc = Solution()
print (abc.lengthOfLongestSubstring(" "))
                