class Solution(object):
    def divide(self, dividend, divisor):
        neg = False
        if dividend < 0:
            neg = not neg
            dividend = -dividend
        if divisor < 0:
            neg = not neg
            divisor = -divisor
            
        ans = 0
        div = divisor
        mul = 1 # multiple times
        while dividend >= divisor:
            if dividend >= div:
                dividend -= div
                ans += mul
                div = div << 1
                mul = mul << 1
            else:
                div = div >> 1
                mul = mul >> 1
                if dividend < div:
                    continue
                dividend -= div
                ans += mul
        
        if neg:
            return max(-ans, -2147483648)
        return min(2147483647, ans)

abc = Solution()
print (abc.divide(5055, 45))