from typing import List
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        level = -1 
        res = 0
        A.sort()
        for x in A:
            if level < x:
                level = x
            else:
                level += 1
                res += level - x
        
        return res

abc = Solution()
print (abc.minIncrementForUnique([3,2,1,2,1,6]))