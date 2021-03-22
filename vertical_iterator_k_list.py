"""
Iterate List of list vertically
tags : Twitter, array
"""

class Solution():
    def vertical_iterator(self, arr):
        ans = []
        arr_len = len(arr)
        col = 0
        
        while True:
            is_empty = True
            for x in range(arr_len):
                if col < len(arr[x]):
                    is_empty = False
                    ans.append(arr[x][col])
            
            if is_empty:
                break

            col += 1
        
        print (ans)

abc = Solution()
abc.vertical_iterator([
    [5,6],
    [7],
    [1,2,3,4],
])

            
            



