from collections import defaultdict
from bisect import bisect

class Solution:
    def shortestWay(self, source, target):
        d = defaultdict(list)
        for i, c in enumerate(source):
            d[c].append(i)
        
        res = 1
        max_idx = -1
        for c in target:
            if c not in d:
                return -1
            
            j = bisect(d[c], max_idx)
            if j >= len(d[c]):
                max_idx = d[c][0]
                res += 1
            else:
                max_idx = d[c][j]
            
        return res

abc = Solution()
abc.shortestWay("edacdedabb", "edabbaedabba")

