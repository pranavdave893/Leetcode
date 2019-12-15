from collections import Counter
class Solution(object):
    def reorganizeString(self, S):
        char_count = Counter(S)
        first = char_count.most_common()[0][0]                
        abcd = [first for _ in range(char_count[first])]

        i = 0

        for chars in char_count:
            if chars != first:
                for _ in range(char_count[chars]):
                    abcd[i%len(abcd)] += chars
                    i += 1
        
        return ''.join(abcd) if i >= len(abcd) - 1 else ''


abc = Solution()
abc.reorganizeString