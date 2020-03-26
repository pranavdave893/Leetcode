from collections import defaultdict

class Solution(object):

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets: return []
        tickets.sort(key=lambda x:x[1])
        graph = defaultdict(list)
        
        for x, y in tickets:
            graph[x].append(y)
        
        ans = []
        
        def dfs(start, ans):
            neighbours = graph[start]
            while neighbours:
                next_dest = neighbours.pop(0)
                dfs(next_dest, ans)
            ans.append(start)
        
        dfs("JFK", ans)
        return ans[::-1]

abc = Solution()
print (abc.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])) # ["JFK","NRT","JFK","KUL"]
print (abc.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print (abc.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))