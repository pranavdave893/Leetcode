class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_square_sum(q):
            t = 0

            while(q!=0):
                r = q % 10
                t += r * r
                q = q / 10

            return t
        
        while(n > 4):
            n  = get_square_sum(n)
            if n == 1:
                return True
        
        if n == 1:
            return True
        return False

abc = Solution()
print (abc.isHappy(2))

                

