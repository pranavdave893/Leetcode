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

# abc = Solution()
# abc.wordBreak("catsanddog",
# ["cat","cats","and","sand","dog"])

class Sol2():
    def tile_possibility(self, tiles):
        res = set()

        ans = []

        def dfs(new_tiles, path):
            if path not in res:
            
                if path:
                    ans.append(path)
                    res.add(path)
                
                for idx in range(len(new_tiles)):
                    dfs(new_tiles[:idx] + new_tiles[idx+1:], path + new_tiles[idx])
        
        dfs(tiles, "")
        return ans

abc = Sol2()
print (abc.tile_possibility("AAB"))
            


class abcd():
    def temp(self, items):
        dct = {}
        
        for x, y in items:
            if x not in dct:
                dct[x] = [y, 1]
            else:
                score, ct = dct[x]
                score += y
                ct += 1
                dct[x] = [score, ct]
        
        print (dct)
        ans = []
        for student, score in dct.items():
            s, ct = score
            ans.append([student, s//ct])
        
        return ans

abc = abcd()
abc.temp([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
