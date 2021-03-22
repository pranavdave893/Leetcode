from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        windowStart, matched = 0, 0
        char_frequency = Counter(s1)

        for windowEnd in range(len(s2)):
            if s2[windowEnd] in char_frequency:
                char_frequency[s2[windowEnd]] -= 1
                if char_frequency[s2[windowEnd]] == 0:
                    matched += 1
            if matched == len(char_frequency):
                return True
            
            if windowEnd >= len(s1) - 1:
                if s2[windowStart] in char_frequency:
                    if char_frequency[s2[windowStart]] == 0:
                        matched -= 1
                    char_frequency[s2[windowStart]] += 1
                windowStart += 1
        return False

abc = Solution()
# print (abc.checkInclusion("abcd", "cxcabd"))
# print (abc.checkInclusion("ab", "eidbaooo"))
print (abc.checkInclusion("adc", "dccdca"))