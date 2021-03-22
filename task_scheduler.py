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

        ans = []
        for tasks, count in task_count.items():
            heappush(heap, (-count, tasks))
        
        while heap:
            new_count = 0
            tmp = []
            for _ in range(cycle):
                if heap:
                    temp = heappop(heap)
                    tmp.append(temp)
                    ans.append(temp[1])
                    new_count += 1
            
            for x, y in tmp:
                x += 1
                if x != 0:
                    heappush(heap, (x, y))
            
            answer += cycle if heap else new_count

        print (ans)
        return answer
    
abc = Solution()
print (abc.leastInterval(["A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"], 1))

