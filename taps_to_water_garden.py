class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """

        ranges = [(i-r,i+r) for i,r in enumerate(ranges)]
        ranges.sort(reverse = True)
        
        watered = 0
        ans = 0
        
        while ranges:
            far_right = []
            while ranges and ranges[-1][0] <= watered:
                far_right.append(ranges.pop()[1])
            if not far_right:
                return -1
            watered = max(far_right)
            ans += 1
            if watered >= n:
                return ans
        return ans

abc = Solution()
abc.minTaps(7, [1,2,1,0,2,1,0,1])


            
            
        
