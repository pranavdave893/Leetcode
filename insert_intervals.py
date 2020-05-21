class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals: return 
        ans = []
        
        nI = newInterval
        is_added = False
        
        for x in intervals:
            changed_pre = False
            pre = ans[-1] if is_added else x
            if is_added:
                if pre[0] <= x[0] <= pre[1]:
                    pre[0] = min(pre[0], x[0])
                    pre[1] = max(pre[1], x[1])
                    changed_pre = True

            elif x[0] <= nI[0] <= x[1]:
                x[0] = min(x[0], nI[0])
                x[1] = max(x[1], nI[1])
                is_added = True

            if not changed_pre:
                ans.append(x)
        
        if not is_added:
            ans.append(newInterval)
        return ans

abc = Solution()

[[1,3],[6,9]],
[2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print (abc.insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [6,8]
print (abc.insert(intervals, newInterval))