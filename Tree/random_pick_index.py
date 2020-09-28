import random
"""
Q : https://leetcode.com/problems/random-pick-index/
A : https://leetcode.com/problems/random-pick-index/discuss/88153/Python-reservoir-sampling-solution. 
"""

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = None
        count = 0
        
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                
                rand = random.randint(1, count)
                if rand == count:
                    res = i
        return res
