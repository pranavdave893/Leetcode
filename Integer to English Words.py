# num_to_eng_dict = {
#             0:'zero',1: 'One', 2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',
#             8:'Eight', 9:'Nine', 10:'Ten', 11: 'Eleven', 12: 'Twelve', 13:'Thriteen', 14:'Fourteen',
#             15:'Fifteen', 16:'Sixteen', 17:'Seventeen',18:'Eighteen', 19: 'Nineteen', 20:'Twenty', 
#             30:'Thrity', 40:'Fourty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80: 'Eighty', 
#             90:'Ninty',
#         }

#         str_num = str(num)

#         def recur(num):
#             if num == 0:
#                 return ''

#             if num <= 20:
#                 return num_to_eng_dict[num]
            
#             if 20 < num < 100:
#                 abc = (num // 10) * 10
#                 ans = num_to_eng_dict[abc] + recur(num % 10)
#                 return ans
            
#             elif 20 < num < 999:
#                 abc = num // 100 
#                 ans = num_to_eng_dict[abc] + " Hundred " + recur(num % 100)
#                 return ans
            
#             elif 1000 <= num < 99999:
#                 abc = num // 1000
#                 ans = num_to_eng_dict[abc] + " Thousand " + recur(num % 1000)
#                 return ans



#         ans = recur(num)
#         return ans

class Solution(object):
    def __init__(self):
        
        self.lessThan20 =["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]
        
        
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        
        res = ""

        for i in range(len(self.thousands)):
        
            if num % 1000 != 0:
                res = self.helper(num%1000) + self.thousands[i] + " " + res
            
            num //= 1000
        
        return res.strip()
    

    def helper(self, num):
        if num == 0:
            return ""
        
        elif num < 20:
            return self.lessThan20[num] + " "
        
        elif num < 100:
            return self.tens[num//10] + " " + self.helper(num%10)
        
        else:
            return self.lessThan20[num//100] + " Hundred " + self.helper(num%100)


abc = Solution()
print (abc.numberToWords(1234567))