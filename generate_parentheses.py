class Solution(object):
    def generateParenthesis(self, n):
        left = right = n
        result = []
        curr = ""
        
        def dfs(left, right, curr, result):
            if left == right == 0:
                result.append(curr)
                return
            
            if left > 0:
                dfs(left-1, right, curr + "(", result)
            
            if left < right:
                dfs(left, right-1, curr + ")", result)
        
        dfs(left, right, curr, result)

        return result




abc = Solution()
print (abc.generateParenthesis(3))
