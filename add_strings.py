class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        from collections import deque
        num1Pointer = len(num1) - 1
        num2Pointer = len(num2) - 1
        
        result = deque()
        carry = 0
        while num1Pointer >= 0 or num2Pointer >= 0:
            num1Dig = ord(num1[num1Pointer]) - ord('0') if num1Pointer >= 0 else 0
            num2Dig = ord(num2[num2Pointer]) - ord('0') if num2Pointer >= 0 else 0
            currentSum = num1Dig + num2Dig + carry
            carry = currentSum // 10
            result.appendleft(str(currentSum % 10))
            num1Pointer -= 1
            num2Pointer -= 1
        
        if carry:
            result.appendleft(str(carry))
        
        return "".join(result)

abc = Solution()
print (abc.addStrings('99', '9'))

"""

112.55
7.9
"""

            




