"""
Q : https://leetcode.com/discuss/interview-question/406663/Bloomberg-or-Phone-Screen-or-Min-Steps-to-Generate-Number
"""
from collections import deque
class Solution():
    def minStep(self, n):
        q = deque([1])
        steps = 0
        visited = set()

        while q:
            no = len(q)
            steps += 1

            for x in range(no):

                curr_num = q.popleft()
                
                if curr_num in visited:
                    continue

                visited.add(curr_num)

                curr_num_2 = curr_num * 2
                curr_num_3 = curr_num // 3

                if curr_num_2 == n or curr_num_3 == n:
                    return steps
                
                q.append(curr_num_2)

                if curr_num_3 > 0:
                    q.append(curr_num_3)

abc = Solution()
print (abc.minStep(121))
