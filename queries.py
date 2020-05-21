class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        P = [i for i in range(1, m+1)]

        ans = []
        
        for i in queries:
            for idx, x in enumerate(P):
                if x == i:
                    ans.append(idx)
                    break
            P = [P[idx]] + [y for y in P if y != P[idx]]
        
        return ans

abc = Solution()
print (abc.processQueries([3,1,2,1], 5))
print (abc.processQueries([4,1,2,2], 4))
print (abc.processQueries([7,5,5,8,3], 8))