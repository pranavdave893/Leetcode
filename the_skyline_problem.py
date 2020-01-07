from collections import defaultdict
from heapq import heappush, heappop

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return buildings
        
        points = []

        for l,r,h in buildings:
            points += [(l, -h), (r, h)]
        
        points.sort()

        result = []
        heights = [0]
        prev = 0

        dct = defaultdict(int)

        for x, h in points:
            if h < 0:
                heappush(heights, h)
            else:
                dct[-h] += 1
            
            while dct[heights[0]] > 0:
                dct[heights[0]] -= 1
                heappop(heights)
            
            curr = heights[0]

            if curr != prev:
                result.append([x, -curr])
                prev=curr
        
        return result

    def test_1(self):
        buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
        answer = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
        assert answer == self.getSkyline(buildings), self.getSkyline(buildings)
    
    def test_2(self):
        buildings = [[2,9,10],[9,12,15]]
        answer = [[2,10],[9,15],[12,0]]
        assert answer == self.getSkyline(buildings), self.getSkyline(buildings)
    
    def test_3(self):
        buildings = [[1,2,1],[1,2,2],[1,2,3]]
        answer = [[1,3],[2,0]]
        assert answer == self.getSkyline(buildings), self.getSkyline(buildings)
    
    def test_4(self):
        buildings = [[0,2,3],[2,4,3],[4,6,3]]
        answer = [[0,3],[6,0]]
        assert answer == self.getSkyline(buildings), self.getSkyline(buildings)
    


abc = Solution()
abc.test_1()
# # abc.test_2()
# # abc.test_3()
# abc.test_4()


        

# if not buildings:
        #     return buildings
        
        # # Critical points where we use negative heights for building's left points
        # points = []
        # for l, r, h in buildings:
        #     points += [(l, -h), (r, h)]
            
        # # Sort critical points where two points have the same x-corrdinates 
        # # will be sorted based on whether they are left or right points.
        # points.sort()
        
        # # Use a heap to store heights where the last height is 0 
        # # and other elements are negative
        # result = []
        # heights = [0]
        # prev = heights[0]
				
        # # Save the heights that will be removed later
        # ignored = defaultdict(int)
        
        # for x, h in points:
        #     if h < 0:
        #         heappush(heights, h)
        #     else:
        #         ignored[-h] += 1

        #     # Remove heights if they become the root of the heap
        #     while ignored[heights[0]] > 0:
        #         ignored[heights[0]] -= 1
        #         heappop(heights)

        #     # The first element is value of the heap's root node                
        #     cur = heights[0]
        #     if cur != prev:
        #         result.append([x, -cur])
        #         prev = cur
        
        # return result