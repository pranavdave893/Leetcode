class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        if not events:return 0
        if len(events) == 1 : return 1
        
        # events.sort()
        
        s, e = events[0][0], events[0][1]
        # print (s, e)
        ans = 1
        
        for x, y in events[1:]:
            if (x,y) == (s, e):
                continue
            if s < x <= e:
                if y > s and y >= e:
                    ans += 1
                    s, e = x, y
                
                elif y <= e:
                    s, e = x, y
            else:
                ans += 1
                s, e = x, y
        print(ans)

abc = Solution()

# abc.maxEvents([[1,2],[2,2],[3,3],[3,4],[3,4]])
# abc.maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]])
# abc.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]])
abc.maxEvents([[1,2],[2,3],[3,4],[1,2]])