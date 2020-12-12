class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def dfs(i, seen):
            for j in range(len(M)):
                if M[i][j] == 1 and j not in seen:
                    seen.add(j)
                    dfs(j, seen)

        seen = set()
        ans = 0
        for i in range(len(M)):
            if i not in seen:
                dfs(i, seen)
                ans += 1
        print (ans)

abc = Solution()
abc.findCircleNum(
    [[1,1,0],
    [1,1,0],
    [0,0,1]])