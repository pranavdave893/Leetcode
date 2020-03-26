class Solution(object):
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
abc.maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]])
