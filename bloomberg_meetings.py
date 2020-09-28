"""
https://leetcode.com/discuss/interview-question/773831/Bloomberg-Virtual-Onsite-NY-Location-July-2020
"""
import heapq
class Solution():
    def find_busy_time(self, times):
        if not times:
            return []
        
        times.sort(key=lambda  x: x[0])

        ans = []

        heap = []

        for x, y in times:

            if not heap:
                heapq.heappush(heap, (-y, x))
            
            elif y < -heap[0][0]:
                
                if not ans:
                    ans.append([heap[0][1], -heap[0][0], True])
                else:
                    continue
            
            elif ans[-1][0] <= x <= ans[-1][1] and y > -heap[0][0]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], y), True]
                heapq.heappop(heap)
                heapq.heappush(heap, (-y, x))
            
            else:
                ans.append([x, y, False])
                heapq.heappop(heap)
                heapq.heappush(heap, (-y, x))

        return [[x, y] for x, y, z in ans if z]

times = [[100, 300], [115, 145], [145, 215], [200, 400], [215, 230], [215, 415], [500, 600], [600, 800]]
abc = Solution()
print (abc.find_busy_time(times))