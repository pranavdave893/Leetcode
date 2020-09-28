class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dct = {'{0}'.format(i):i for i in range(10)}

        n1_s = len(num1) - 1
        n2_s = len(num2) - 1
        sum_string = []
        carry = 0
        while (n2_s >= 0 and n1_s >= 0):
            
            temp = dct[num2[n2_s]] + dct[num1[n1_s]] + carry

            if temp > 10:
                temp = temp % 10
                carry = 1
            
            sum_string.append('%s' %temp)
            n2_s -= 1
            n1_s -= 1
        
        return ''.join(sum_string[::-1])

abc = Solution()
print (abc.addStrings('1234', '456'))

            




