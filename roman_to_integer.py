class Solution(object):
    def romanToInt(self, S):
        table = {
            'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400,
            'CM':900
        }
        
        sum = 0
        x = 0
        while x < len(S):
            if x+1 <= len(S)-1:
                num = S[x] + S[x+1]
                if num in table:
                    sum += table[num]
                    x += 2
                else:
                    sum += table[S[x]]
                    x +=1
            else:
                sum += table[S[x]]
                x +=1
        
        print (sum)

abc = Solution()
abc.romanToInt("MMMXLV")
                

