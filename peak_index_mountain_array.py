class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        left = 0
        right = len(A)-1
        while left <= right:
            mid = left + (right-left)/2
            if A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

abc = Solution()
print (abc.peakIndexInMountainArray([0,2,1,0]))