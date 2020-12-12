
import heapq
from math import sqrt
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        for x,y in points:
            heapq.heappush(heap, [-(x*x + y*y),[x,y]])
            if len(heap) > K:
                heapq.heappop(heap)
        
        return [pair for distance, pair in heap]

abc = Solution()
abc.kClosest([[-5,4],[-3,2],[0,1],[-3,7],[-2,0],[-4,-6],[0,-5]], 6)
