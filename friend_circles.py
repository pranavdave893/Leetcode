class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        seen = set()
        ans = 0

        def dfs(i):
            for j in range(len(M)):
                if M[i][j] == 1 and j not in seen:
                    seen.add(j)
                    dfs(j)

        for i in range(len(M)):
            if i not in seen:
                dfs(i)
                ans += 1
        print (ans)

abc = Solution()
abc.findCircleNum(
    [[1,1,0],
    [1,1,0],
    [0,0,1]])