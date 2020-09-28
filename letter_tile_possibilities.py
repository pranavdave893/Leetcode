"""
Q: https://leetcode.com/problems/letter-tile-possibilities/
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def dfs(path, tiles2):
            if path not in res:
                if path:
                    res.add(path)
                for i in range(len(tiles2)):
                    dfs(path+tiles2[i], tiles2[:i] + tiles2[i+1:])
        
        dfs("", tiles)
        return len(res)


abc = Solution()
print (abc.numTilePossibilities("ABC"))
        

        