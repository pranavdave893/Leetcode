class Solution(object):
    def wordBreak(self, s, wordDict):
        dct = {key:True for key in wordDict}

        def is_word_indict(word_str):
            return word_str in wordDict

        def findword(strn):
            if strn in dct:
                return dct[strn]
            
            if strn == "":
                return True
            
            s = ""
            for x in range(len(strn)):
                s = s + strn[x]
                if is_word_indict(s):
                    res = findword(strn[x+1:])
                    if res:
                        dct[s] = True
                        return True
            dct[s] = False
            return False
        return findword(s)
abc = Solution()
strn = "aaaab"
word_dict = ["a","aa","aaa","aaaa","aaaab"]
# strn = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# word_dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print (abc.wordBreak(strn, word_dict))
