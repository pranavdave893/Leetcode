from heapq import heapify, heappush, heappop
class Solution(object):

    def assignBikes(self, workers, bikes):
        manhatten_dist = lambda w,b : abs(w[0]-b[0]) + abs(w[1]-b[1])
        distances = [-1 for x in range(len(workers))]

        for i, w in enumerate(workers):
            queue = []
            for j, b in enumerate(bikes):
                distance = manhatten_dist(w, b)
                queue.append((distance, i, j))
            heapify(queue)
            distances[i] = queue
        
        w_to_b = {}
        paths = [heappop(distance) for distance in distances]
        heapify(paths)
        visited = set()

        while len(visited) < len(workers):
            distance, w, b = heappop(paths)
            if w not in w_to_b and b not in visited:
                w_to_b[w] = b
                visited.add(b)
            else:
                heappush(paths, heappop(distances[w]))
        
        return [w_to_b[b] for b in sorted(w_to_b)]
    
    def assignBikes_bucketSort(self, workers, bikes):
        # https://www.youtube.com/watch?time_continue=416&v=Ej9R8SxP9c0&feature=emb_title
        # https://leetcode.com/problems/campus-bikes/discuss/343953/Java-Solution-using-Bucket-Sort-with-Video-Explanation
        
        distances = [[] for _ in range(2001)]

        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx-bx) + abs(wy-by)
                distances[dist].append((i, j))
        
        ans = [-1] * len(workers)
        visited = set()

        for pairs in distances:
            for w, b in pairs:
                if ans[w] == -1 and b not in visited:
                    ans[w] = b
                    visited.add(b)
        
        return ans

                
                

abc = Solution()
print (abc.assignBikes_bucketSort([[3,4],[2,3],[4,2]], [[1,3],[3,3],[2,2],[4,3]]))


            




