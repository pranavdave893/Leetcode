"""
https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28
"""
class Solution(object):
    def permutation(self, items):
        n = len(items)
        ans = []
        used = [False] * n
        
        def printPermutation(items, n, k, depth, curr, ans, used):
            if depth == k:
                ans.append(curr[::])
                return
            
            for i in range(n):
                if not used[i]:
                    curr.append(items[i])
                    used[i] = True
                    print (curr)
                    printPermutation(items, n, k, depth+1, curr, ans, used)
                    print (curr.pop())
                    used[i] = False
            return

        printPermutation(items, n, n, 0, [], ans, used)
        return ans

abc = Solution()
print (abc.permutation([1,2,3]))
