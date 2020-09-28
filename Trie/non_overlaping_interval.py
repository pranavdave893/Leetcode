"""
https://leetcode.com/problems/non-overlapping-intervals/
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        
        end = float('-inf')
        answer = 0
        for it in intervals:
            if it[0] >= end:
                end = it[1]
            else:
                answer +=1
        
        return answer
                