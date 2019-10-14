class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #here we need a global wise list, each time we just append to the result
        rslt=[]
        
        def dfs(temp, elements):
            #gather rslt
            if len(elements)==0:
                rslt.append(temp[:]) #still remember to use temp[:]
            for e in list(set(elements)): #this is the only difference
                temp.append(e)
                #backtrack
                next_elements=elements[:]
                next_elements.remove(e)
                dfs(temp, next_elements)
                import pdb; pdb.set_trace()
                temp.pop()
                
                
        dfs([],nums)
        return rslt

abc = Solution()
print (abc.permuteUnique([1,1,2]))