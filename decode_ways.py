# # DP Bottom up O(1) Space : https://leetcode.com/problems/decode-ways/discuss/30637/Python-DP-solution

# abc = "123"

# decode_pointer = 0
# dp = [-1] * len(abc)

# def is_valid(substr):
#     if len(substr) == 0 or substr.find('0') == 0:
#         return False
    
#     return int(substr) >= 1 and int(substr) <= 26

# def recur(abc, decode_pointer):
#     if decode_pointer >= len(abc):
#         return 1

#     if dp[decode_pointer] > -1:
#         return dp[decode_pointer]


#     answer = 0
#     for i in range(1,3):
#         if decode_pointer + i <= len(abc):
#             substr = abc[decode_pointer:decode_pointer + i]
#             if is_valid(substr):
#                 answer += recur(abc, decode_pointer+i)
    
#     dp[decode_pointer] = answer
#     return dp[decode_pointer]

# print (recur(abc, 0))

class SolutionRecur:
    
    def __init__(self):
        self.memo = {}
    
    
    def recur(self, index, s):
        
        if index == len(s):
            return 1
        
        if s[index] == '0':
            return 0
        
        if index == len(s)-1:
            return 1
        
        if index in self.memo:
            return self.memo[index]
        
        ans = self.recur(index+1, s)
        
        if int(s[index : index + 2]) <= 26:
            ans += self.recur(index+2, s)
        
        self.memo[index] = ans
        
        return ans
        
    
    def numDecodings(self, s: str) -> int:
        
        if not s:
            return 0
        
        return self.recur(0, s)

class Solution(object):
    # Bottom Up approch.
    def decodeWays(self, s):
        dp = [0] * (len(s) + 1)

        dp[0] = 1

        dp[1] = 1 if '1' <= s[0] <= '9' else 0
        for i in range(2, len(dp)):
            if '1' <= s[i-1] <= '9':
                dp[i] += dp[i-1]
            
            if '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]
        
        return dp[-1]

abc = Solution()
print (abc.decodeWays('20'))

