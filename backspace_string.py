"""
https://leetcode.com/problems/backspace-string-compare/
"""

class Solution:
    def backspaceCompare(self,S,T):
        len_s = len(S)-1
        len_t = len(T)-1

        count_s = count_t = 0

        while len_s >= 0 or len_t >= 0:
            
            while(len_s >=0):
                if S[len_s]== "#":
                    count_s += 1
                    len_s -= 1
                elif S[len_s] != '#' and count_s > 0:
                    len_s -= 1
                    count_s -= 1
                else:
                    break
                

            while(len_t >=0):
                if T[len_t] == "#":
                    count_t += 1
                    len_t -= 1
                elif T[len_t] != '#' and count_t > 0:
                    len_t -= 1
                    count_t -= 1
                else:
                    break
            
            if (len_s <0 and len_t >=0) or (len_t <0 and len_s >=0):
                return False
            if (len_s >=0 and len_t >=0) and S[len_s] != T[len_t]:
                return False
            
            len_s -= 1
            len_t -= 1
        return True

abc = Solution()
print (abc.backspaceCompare("bxj##tw","bxo#j##tw"))

