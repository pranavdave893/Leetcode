class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        for it in intervals[::-1]:
            if it[0] <= newInterval[1] and it[1] >= newInterval[0]:
                newInterval = [min(newInterval[0], it[0]), max(it[1], newInterval[1])]
            else:
                answer.append(it)
        
        answer.append(newInterval)
        answer.sort(key=lambda x:x[0])
        print (answer)

abc = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
abc.insert(intervals, newInterval)

intervals = [[1,3],[6,9]]
newInterval = [2,5]
abc.insert(intervals, newInterval)