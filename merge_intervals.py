# https://leetcode.com/problems/merge-intervals/discuss/350272/Python3-Sort-O(Nlog(N))
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))
        new_interval = []

        for i in intervals:
            if not new_interval or new_interval[-1][-1] < i[0]:
                new_interval.append(i)
            else:
                new_interval[-1][-1] = max(new_interval[-1][-1], i[1])
        
        return new_interval
        
        


abc = Solution()
print (abc.merge([[1,3],[2,6],[8,10],[15,18]]))
print (abc.merge([[1,4],[4,5]]))
print (abc.merge([[1,3],[1,4],[2,6]]))