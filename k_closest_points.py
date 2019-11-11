from math import sqrt
from heapq import heappush, heappop, heappushpop
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def stupid_python(points, K):
            dct = {}
            answer = []

            for point in points:
                dist = sqrt((0-point[0]) * (0-point[0]) + (0 - point[1]) * (0-point[1]))
                if dist not in dct:
                    dct[dist] = [point]
                else:
                    dct[dist].append(point) 
            
            count = 0
            for value in sorted(dct.items(), key=lambda x:x[0]):
                for points in value[1]:
                    if count == K:
                        break
                    answer.append(points)
                    count += 1
        
            print(answer)
        
        def heap_python(points, K):
            distance = []

            for (x,y) in points:
                dist = -(x*x + y*y)
                if len(distance) == K:
                    heappushpop(distance, (dist, x, y))
                else:
                    heappush(distance, (dist, x, y))
            
            print [[x,y] for (dist, x, y) in distance]
        
        stupid_python(points, K)
        heap_python(points, K)



ip = [[1,3],[-2,2]]
k1 = 1
ip_2 = [[3,3],[5,-1],[-2,4]]
k2 = 2
ip3 = [[1,0],[0,1]]
k3 = 2
abc = Solution()
abc.kClosest(ip, k1)
abc.kClosest(ip_2, k2)
abc.kClosest(ip3, k3)