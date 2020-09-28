from collections import Counter
class Solution(object):
    def sliding(self, n, operations):
        # ROW = len(matrix)
        # COL = len(matrix[0])

        # ans = Counter()
        # for x in range(len(matrix)):
        #     for y in range(len(matrix[0])):
        #         ans[matrix[x][y]] += 1
        
        # new_ans = []

        # for x, y in sorted(ans.items(), key=lambda item: item[1]):
        #     for i in range(y):
        #         new_ans.append(x)
        
        # new_ans = new_ans[::-1]     
        # print (new_ans)
        
        
        
        
        # ctr = 0
        # for line in range(1, (ROW + COL)) : 
        #     # Get column index of the first element 
        #     # in this line of output. The index is 0 
        #     # for first ROW lines and line - ROW for 
        #     # remaining lines  
        #     start_col = max(0, line - ROW) 
    
        #     # Get count of elements in this line. 
        #     # The count of elements is equal to 
        #     # minimum of line number, COL-start_col and ROW  
        #     count = min(line, (COL - start_col), ROW) 
    
        #     # Print elements of this line  
        #     for j in range(0, count) : 
        #         matrix[min(ROW, line) - j - 1][start_col + j] = new_ans[ctr]
        #         ctr += 1
        
        # print (matrix)

        from collections import deque
        ans = [0] * n
        zero_p = deque([0])
        # am kar
        # zero_p = deque()
        # zero_p.append(0)

        # print operations kar to 
        for x in operations:
            if x == "L":
                ptr = zero_p.popleft()
                ans[ptr] = 1
                
                zero_p.append(ptr+1)
            
            elif x[0] == "C":
                # what if it is C10 or C100
                num = int(x[1:])
                ans[num] = 0
                
                # check if the first zero pointer's index is greater than the changed pointer.
                if zero_p and zero_p[0] > num:
                    zero_p.appendleft(num)
                else:
                    zero_p.append(num)
        
        print(ans)


abc = Solution()
# abc.sliding([[1,4,-2], [-2,3,4], [3,1,3]])
abc.sliding(2, ["L", "L", "L", "C1"])