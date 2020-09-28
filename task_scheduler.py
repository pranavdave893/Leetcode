from collections import Counter
from heapq import heappush, heappop
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        if n == 0:
            return len(tasks)
        
        task_count = Counter(tasks)

        heap = []
        cycle = n + 1
        answer = 0

        for tasks, count in task_count.items():
            heappush(heap, -count)
        
        while heap:
            new_count = 0
            tmp = []
            for _ in range(cycle):
                if heap:
                    tmp.append(heappop(heap))
                    new_count += 1
            
            for x in tmp:
                x += 1
                if x != 0:
                    heappush(heap, x)
            
            answer += cycle if heap else new_count

        return answer
    
abc = Solution()
print (abc.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))

