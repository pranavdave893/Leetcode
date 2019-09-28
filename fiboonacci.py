class Solution(object):
    def fib(self,number):
        if number < 0 : raise ValueError("Negative not Allowed.")
        if number == 0: return 0

        if number == 1: return 1

        return self.fib(number-1) + self.fib(number-2)
    
    def fib_dp(self, n):
        fib_array = [0,1]

        while len(fib_array) < n + 1:
            fib_array.append(0)
        
        if n <= 1: return n
        
        import pdb; pdb.set_trace()
        if fib_array[n-1] == 0: fib_array[n-1] = self.fib_dp(n-1)

        if fib_array[n-2] == 0: fib_array[n-2] = self.fib_dp(n-2)

        return fib_array[n-2] + fib_array[n-1]

abc = Solution()
# print abc.fib(100)
print abc.fib_dp(10)

