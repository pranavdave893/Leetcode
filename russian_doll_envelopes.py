class Solution(object):
    def maxEnvelopes_2(self, envelopes):
        import bisect
        if not envelopes:return 0
        envelopes.sort(key=lambda x : (x[0], -x[1]))
        
        ans = []
        
        for x,y in envelopes:
            idx = bisect.bisect_left(ans, y)
            if idx == len(ans):
                ans.append(y)
            elif ans[idx-1] < y:
                ans[idx] = y
        return len(ans)
    
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:return 0
        envelopes.sort(key=lambda x:(x[0],x[1]))
        
        res = [1] * len(envelopes)
        ans = 1

        for i in xrange(1, len(envelopes)):
            for j in xrange(0, i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    res[i] = max(res[i], res[j] + 1)
            
            ans = max(ans, res[i])
        
        print (ans)

abc = Solution()
abc.maxEnvelopes_2([[46,89],[50,53],[52,68],[72,45],[77,81]])
