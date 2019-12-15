class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dct = {}
        for x,y in enumerate(order):
            dct[y] = x
        
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            
            for s1, s2 in zip(w1, w2):
                if dct[s1] < dct[s2]:
                    break
                else:
                    return False
        
        return True

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
abc = Solution()
abc.isAlienSorted(words, order)