# def toString(List): 
#     return ''.join(List) 
  
# def permute(a, l, r): 
#     if l==r: 
#         print toString(a) 
#     else: 
#         for i in xrange(l,r):
#             a[l], a[i] = a[i], a[l] 
#             permute(a, l+1, r) 
#             a[l], a[i] = a[i], a[l] # backtrack 
  
# # Driver program to test the above function 
# string = "ABC"
# n = len(string) 
# a = list(string) 
# permute(a, 0, n) 

class Solution(object):
    def permutation(self, nums):
        result = []
        def permute(a,l, r):
            if l == r:
                result.append(a[:])
            else:
                for i in xrange(l,r):
                    if a[l] != a[i]:
                        a[l], a[i] = a[i],a[l]
                    permute(a, l+1, r)
                    a[l],a[i] = a[i],a[l]
        
        permute(list(set(nums)),0,len(nums)-1)
        # result = set(map(tuple, result))
        # result = map(list, result)
        return result

abc = Solution()
print (abc.permutation([1,1,2]))