"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""
class Solution(object):
    def sequentialDigits(self, low, high):
        
        ans = []
        for start in xrange(1, 10):
            for end in xrange(start, 10):
                cand = int("".join(str(d) for d in xrange(start, end+1)))
                if low <= cand <= high:
                    ans.append(cand)
        ans.sort()
        return ans
