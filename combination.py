class Solution(object):
    def combine(self, n, k):
        ans = []
        def dfs(list_start, list_end, k, start, depth, curr, ans):
            
            if depth == k:
                ans.append(curr[::])
            
            for i in range(start, list_end):
                curr.append(list_start+i)
                dfs(list_start, list_end, k, i+1, depth+1, curr, ans)
                curr.pop() # backtrack
        
        dfs(1,n, k, 0, 0, [], ans )
        return ans



abc = Solution()
print (abc.combine(4,3))