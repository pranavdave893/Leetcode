class Solution(object):
    def wordBreak(self, s, wordDict):
        
        wordDict = set(wordDict)
        self.res = []

        def dfs(s, path):
            if not s:
                self.res.append(path)
                return
            
            for i in range(1, len(s)+1):
                word = s[:i]
                
                if word in wordDict:
                    new_path = path +' '+ word if path else word
                    dfs(s[i:], new_path)
        
        dfs(s, "")
        return self.res
    
    def wordBreak_dp(self, s, wordDict):
        # DFS + Memo
        wordDict = set(wordDict)
        backup = {}
        def DFS(s):
            if not s:
                return ['']
            if s not in backup:
                backup[s]= []
                for i in range(1, len(s)+1):
                    word = s[:i]
                    if word in wordDict:
                        # sentences = DFS(s[i:])
                        for ss in DFS(s[i:]):
                            backup[s].append(word + ' ' + ss) 
            return backup[s]
        DFS(s)
        return [bu[:-1] for bu in backup[s]]
    
    def wordBreak_fast(self, s, wordDict):
        self.length = sorted(list(set([len(word) for word in wordDict])))
        self.dct = {i:set() for i in self.length}

        for word in wordDict:
            self.dct[len(word)].add(word)
        
        return self.find(s, {})

    def find(self, s, cache):
        if s in cache:
            return cache[s]

        res = []

        for l in self.length:
            ch = s[:l]
            if ch in self.dct[l]:
                if l < len(s):
                    for word in self.find(s[l:], cache):
                        res.append(ch + ' ' + word)
                else:
                    res.append(ch)
                    break
        
        cache[s] = res
        return res

abc = Solution()
print (abc.wordBreak_dp("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
