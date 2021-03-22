class Solution():
    def compressArray(self, nums):
        if not nums:
            return []
        

        nums.sort()

        start = nums[0]
        end = nums[0]
        ans = []
        
        for idx, i in enumerate(nums[1:]):
            if i - 1 == start or i-1 == end:
                end = i
            
            elif start != end:
                ans.append("{0} - {1}".format(start, end))
                start, end = i, i
            
            else:
                ans.append(str(start))
                if idx == len(nums)-2:
                    ans.append(str(i))
                start = i
                end = i
        
        if not ans or start != end:
            ans.append("{0} - {1}".format(start, end))
        
        print (ans)
    
    def compressArray_2(self, nums):

        i, j = 0, 0

        nums.sort()
        ans = []
        n = len(nums)

        while (i < n):
            j = i

            while (j + 1 < n) and (nums[j+1] == nums[j] + 1):
                j += 1
            

            if (i == j):
                ans.append(str(nums[i]))

                i += 1
            
            else:
                ans.append("{0}-{1}".format(nums[i], nums[j]))
                i = j + 1
        
        print (ans)



abc = Solution()
abc.compressArray([7,8,9,15,16,20,25])
abc.compressArray([7, 8, 9, 15, 16, 24, 25, 27, 28, 29, 32, 33, 35, 40, 41])
abc.compressArray([1,2,3,4,5,6])

abc.compressArray_2([7,8,9,15,16,20,25])
abc.compressArray_2([7, 8, 9, 15, 16, 24, 25, 27, 28, 29, 32, 33, 35, 40, 41])
abc.compressArray_2([1,2,3,4,5,6])