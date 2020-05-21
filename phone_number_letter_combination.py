class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return res
        dic = {'2' : 'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6':'mno',\
                  '7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        self.dfs("", 0, res, digits, dic)
        return res
    
    def dfs(self, path, index, res, digits, dic):
        if len(path) == len(digits):
            res.append(path)
            return
        
        for x in range(index, len(digits)):
            for y in dic[digits[x]]:
                self.dfs(path+y, x+1, res, digits, dic)

abc = Solution()
print (abc.letterCombinations('23'))