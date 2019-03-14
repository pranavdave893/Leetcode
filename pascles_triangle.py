class Solution:
    def generate(self,numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        """
        Better Solution 
        
        output = [[1] * (i+1) for i in range(numRows)]
        if numRows > 2:
            for row in range(2,numRows):
                width = len(output[row])
                for col in range(1,width-1):
                    output[row][col] = output[row-1][col-1] + output[row-1][col]
        return output
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        temp = self.generate(numRows-1)
        answer = temp
        i = 0 
        answer.append([1])
        while((i+1) < len(temp[numRows-2])):
            answer[numRows-1].append(temp[numRows-2][i]+temp[numRows-2][i+1])
            i += 1
        answer[numRows-1].append(1)

        return answer

abc = Solution()
print(abc.generate(5))