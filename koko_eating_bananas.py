class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """

        if H == len(piles):
            return max(piles)
        
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = lo + (hi-lo)/2
            h = 0
            for x in piles:
                if x != mid:
                    h = h + x / mid + 1
                else:
                    h = h + 1
            if h <= H:
                hi = mid
            else:
                lo = mid + 1
        return lo

abc = Solution()
print (abc.minEatingSpeed([30,11,23,4,20], 5))