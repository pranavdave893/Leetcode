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
        while (n2_s => 0 and n1_s => 0):
            
            temp = dct[n2_s] + dct[n1_s] + carry

            if temp > 10:
                temp = temp % 10
                carry = 1
            
            sum_string.append('%s' %temp)

            




