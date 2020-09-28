from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= (n-i):
                return n-i
        return 0

abc = Solution()
print (abc.hIndex([10,12,15,16,25]))