class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Approch 1 : https://leetcode.com/problems/maximum-product-subarray/discuss/402220/Python-O(n)
        Approch 2 : Two pass :
            https://leetcode.com/problems/maximum-product-subarray/discuss/370656/Simple-solution-with-detailed-explanation-Python
        """
        
        imax = nums[0]
        imin = nums[0]
        answer = nums[0]
        import pdb; pdb.set_trace()
        for x in nums[1:]:
            current = x
            imax, imin = max(current, imax*current,imin*current), min(current, imax*current, imin*current)            
            answer = max(answer, imax)
        return answer

abc = Solution()
# print (abc.maxProduct([-2]))
# print (abc.maxProduct([2,3,-2,4]))
# print (abc.maxProduct([-2,0,-1]))
# print (abc.maxProduct([-5,0,1,2,3,-2,7,14]))
# print (abc.maxProduct([-2,3,-4]))
print (abc.maxProduct([-7,-2,-4])) 
