from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        word_dict = set(wordDict)
        
        memo = {}
        
        def dfs(s):
            
            if s in memo:
                return memo[s]
            
            if not s:
                return ['']
            
            memo[s] = []
            
            for i in range(1, len(s)+1):
                word = s[:i]
                
                if word in word_dict:
                    
                    for next_str in dfs(s[i:]):
                        memo[s].append(word + " " + next_str)
            return memo[s]
        
        dfs(s)
        
        return [x[:-1] for x in memo[s]]

abc = Solution()
abc.wordBreak("catsanddog",
["cat","cats","and","sand","dog"])