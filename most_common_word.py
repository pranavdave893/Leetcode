from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.split(" ")
        
        dct = {}
        
        import pdb; pdb.set_trace()
        for word in paragraph:
            word = word.lower().strip(",;'/\:;")
            if word not in banned:
                if word in dct:
                    dct[word] +=1
                else:
                    dct[word] = 1
        print (dct)
        max_value = 0
        for key,value in dct.items():
            if value > max_value:
                answer = key
                max_value = value
        
        print(answer)

para = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = "hit"
abc = Solution()
abc.mostCommonWord(para, banned)