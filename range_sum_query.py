class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0]
        for n in nums:
            self.dp.append(self.dp[-1] + n)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1] - self.dp[i]

abc = NumArray([-2, 0, 3, -5, 2, -1])
abc.sumRange(1,3)