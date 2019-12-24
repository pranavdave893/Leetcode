class Solution(object):
# @return a string
    def fractionToDecimal_1(self, numerator, denominator):
        res=""
        if numerator/denominator < 0:
            res += "-"
        
        if numerator % denominator == 0:
            return str(numerator/denominator)

        numerator=abs(numerator)
        denominator=abs(denominator)
        
        res += str(numerator/denominator)
        res += "."

        numerator%=denominator
        dct = {}
        i = len(res)

        while numerator!= 0:
            if numerator not in dct.keys():
                dct[numerator] = i
            else:
                i=dct[numerator]
                res = res[:i] + "(" + res[i:] + ")"
                return res
            numerator = numerator * 10
            res += str(numerator/denominator)
            numerator %= denominator
            i += 1
        
        return res

abc = Solution()
print (abc.fractionToDecimal_1(22, 7))