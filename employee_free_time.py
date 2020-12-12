"""
https://leetcode.com/problems/employee-free-time/solution/
tags : Facebook, phone
"""
class Solution:
    def employeeFreeTime(self, schedule):
        
        # O(N Log(N)) where N is number of intervals =
        if not schedule: return []
        
        intervals = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        
        ans = []
        
        start = intervals[0]
        
        for x in intervals[1:]:
            if start.end < x.start:
                ans.append(Interval(start.end, x.start))
                start = x
            
            elif x.end > start.end:
                start = x
        
        return ans
    

    def empfreetime(self, schedule):
        import heapq
        heap = []

        for emp in schedule:
            for i in emp:
                heap.append((i.start, i.end))
        
        heapq.heapify(heap)


        start, end = heapq.heappop(heap)

        free = end
        res = []

        while heap:
            start, end = heapq.heappop(heap)

            if start > free:
                res.append(Interval(free, start))
                free = end
            
            else:
                free = max(free, end)
        
        return res