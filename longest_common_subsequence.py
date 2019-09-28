class Solution:
    def longestCommonSubsequence(self, str1, str2):
        # m = len(str1)
        # n = len(str2)

        def recur(str1, str2, m, n):
            
            if m < 0 or n < 0:
                return 0
            
            if str1[m] == str2[n]:
                return 1 + recur(str1, str2, m-1, n-1)
            
            else:
                return max(recur(str1, str2, m-1, n),recur(str1, str2, m, n-1))

        def dp(str1, str2):
            m = len(str1)
            n = len(str2)

            dp_matrix = [[0 for x in range(n+1)] for y in range(m+1)]

            for i in xrange(1,m+1):
                for j in xrange(1,n+1):
                    if str1[i-1] == str2[j-1]:
                        dp_matrix[i][j] = 1 + dp_matrix[i-1][j-1]
                    else:
                        dp_matrix[i][j] = max(dp_matrix[i-1][j], dp_matrix[i][j-1])

            return dp_matrix[m][n]
        
        return dp(str1, str2)


abc = Solution()
print abc.longestCommonSubsequence('ylqpejqbalahwr', 'yrkzavgdmdgtqpg')
        