"""
https://leetcode.com/problems/course-schedule-ii/discuss/385683/Clean-Python-Kahn's-Alg-with-In-degree-Attribute

"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = {}
        graph = {x:[] for x in range(numCourses)}
        for courses, pre in prerequisites:
            graph[pre].append(courses)
        
        for x, neighbour in graph.items():
            indegree.setdefault(x, 0)
            for n in neighbour:
                indegree[n] = indegree.get(n, 0) + 1
 
        empty = {v for v,count in indegree.items() if count == 0}
        result = []

        while empty:
            v = empty.pop()
            result.append(v)

            for neighbour in  graph.get(v, []):
                indegree[neighbour] -= 1
        
                if indegree[neighbour] == 0:
                    empty.add(neighbour)
            
        return False if len(result) != len(indegree) else result

abc = Solution()
# print (abc.canFinish(12,[
#     [8,10],
#     [0, 8],
#     [0,10],
#     [0, 2],
#     [2,4],
#     [4,5],
#     [5,6],
#     [1,6],
#     [3,6],
#     [2,3],
#     [2,1],
#     ]
#     ))

print (abc.canFinish(3,[[1,0]]))