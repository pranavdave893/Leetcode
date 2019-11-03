# DP Bottom up O(1) Space : https://leetcode.com/problems/decode-ways/discuss/30637/Python-DP-solution

abc = "123"

decode_pointer = 0
dp = [-1] * len(abc)

def is_valid(substr):
    if len(substr) == 0 or substr.find('0') == 0:
        return False
    
    return int(substr) >= 1 and int(substr) <= 26

def recur(abc, decode_pointer):
    if decode_pointer >= len(abc):
        return 1

    if dp[decode_pointer] > -1:
        return dp[decode_pointer]


    answer = 0
    for i in range(1,3):
        if decode_pointer + i <= len(abc):
            substr = abc[decode_pointer:decode_pointer + i]
            if is_valid(substr):
                answer += recur(abc, decode_pointer+i)
    
    dp[decode_pointer] = answer
    return dp[decode_pointer]

print (recur(abc, 0))
        

