from collections import defaultdict
class Solution(object):
    def abcd(self, lst):

        graph = defaultdict(list)

        for x, y in lst:
            graph[x].append(y)
            graph[y].append(x)
        
        ans = []
        seen = set()

        def dfs(node):
            if node in seen: return
            for items in graph[node]:
                if items not in temp:
                    temp.add(items)
                    dfs(items)
                    seen.add(items)


        temp = set()
        for x, y in lst:
            temp.add(x)
            dfs(x)
            seen.add(x)
            ans.append(list(temp))
            temp = set()
        
        ans = sorted(ans, key=lambda i :(-len(i), i ))
        return ans[0]
        

abc = Solution()
print (abc.abcd(
[["I1", "I2"],
["I3", "I4"],
["I4", "I5"]]
))

print (abc.abcd(
[["Item1", "Item2"],
["Item3", "Item4"]]
))
