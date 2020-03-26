class Solution(object):
    def minFallingPathSum(self, A):
        if not A: return 0

        if len(A) < 2 : return min(A)

        curr_ans, ans= float('inf'), 0
        next_row = 0

        def dfs(A, curr_col, ans, current_ans):
            if not A: return ans
            for j in range(len(A[0])):
                for i in range(len(A)):
                    if not j - curr_col > 1:
                        ans += A[i][j]
                        next_ans = dfs(A[1:], j, ans, current_ans)
                        if next_ans:
                            current_ans = min(current_ans, next_ans)
                        else:
                            current_ans = min(current_ans, ans)
                
                if not j - curr_col > 1:
                    ans -= A[i][j]
            
            return current_ans

        dfs(A, 0, 0, float('inf'))

abc = Solution()
abc.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])