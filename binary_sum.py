class Solution(object):
    def convert_to_int(self,number):
        power = 0
        # import pdb; pdb.set_trace()
        num =0
        for i in number[::-1]:
            num += int(i)*(2**power)
            power+=1
        return num
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if int(a) is 0 and int(b) is 0:
            return '0'
        abc = Solution()
        
        new_num=abc.convert_to_int(a) + abc.convert_to_int(b)
        print new_num
        stack = []
        while new_num > 0:
            stack.insert(0,new_num%2)
            new_num = new_num//2
            
        print stack
        return int(''.join(map(str,stack)))

xyz = Solution()
print xyz.addBinary('111','1')
    