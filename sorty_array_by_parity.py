class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0 
        j = len(A)-1
        
        if i==j:
            return A
        
        def is_even(number):
            if number%2 == 0:
                return True
        
        def is_odd(number):
            if number%2 != 0:
                return True
            
        while i!=j and i<j and j>i:
            if is_even(A[i]) and is_odd(A[j]):
                i +=1
                j -=1
                continue
            if is_odd(A[i]) and is_even(A[j]):
                A[i],A[j] = A[j],A[i]
                i +=1
                j -=1
                continue
            if is_even(A[i]) and is_even(A[j]):
                A[i+1],A[j] = A[j],A[i+1]
                i += 1
                continue
            if is_odd(A[i]) and is_odd(A[j]):
                A[j-1],A[i] = A[i], A[j-1]
                j -=1
                continue
        return A

abc = Solution()
A = [3,1,2,4]
print (abc.sortArrayByParity(A))