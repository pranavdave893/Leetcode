
# def recur(num):
#     num_to_eng_dict = {
#     0:'zero',1: 'One', 2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',
#     8:'Eight', 9:'Nine', 10:'Ten', 11: 'Eleven', 12: 'Twelve', 13:'Thriteen', 14:'Fourteen',
#     15:'Fifteen', 16:'Sixteen', 17:'Seventeen',18:'Eighteen', 19: 'Nineteen', 20:'Twenty', 
#     30:'Thrity', 40:'Fourty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80: 'Eighty', 
#     90:'Ninty',
# }
#     if num == 0:
#         return ''

#     if num <= 20:
#         return num_to_eng_dict[num]
    
#     if 20 < num < 100:
#         abc = (num // 10) * 10
#         ans = num_to_eng_dict[abc] + recur(num % 10)
#         return ans
    
#     elif 20 < num < 999:
#         abc = num // 100 
#         ans = num_to_eng_dict[abc] + " Hundred " + recur(num % 100)
#         return ans
    
#     elif 1000 <= num < 9999:
#         abc = num // 1000
#         ans = num_to_eng_dict[abc] + " Thousand " + recur(num % 1000)
#         return ans
    
#     elif 10000 <= num < 99999:
#         abc = num // 10000
#         ans = num_to_eng_dict[abc] + " Thousand " + recur(num % 1000)
#         return ans



# print (recur(1234))

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


class Solution_2:
    
    ones = ["Zero", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
    tens = ["", "", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
    digits = [" Hundred", " Thousand", " Million", " Billion"]
    
    
    def numberToWords(self, num: int) -> str:
        if not num:
            return self.ones[num]
        
        res = ""
        counter = 0
        
        while True:
            temp_num = num % 1000
            num = num // 1000
            ones_place, tens_place, hun_place = temp_num % 10, (temp_num % 100) // 10, (temp_num % 1000) // 100
            
            if counter > 0 and temp_num:
                res = self.digits[counter] + res
            
            if tens_place < 2:
                res = (self.ones[temp_num % 100] if temp_num % 100 else "") + res
            else:
                res = self.tens[tens_place] + (self.ones[ones_place] if ones_place else "") + res
            
            if hun_place:
                res = self.ones[hun_place] + self.digits[0] + res
            
            counter += 1
            if num <= 0:
                break
        
        return res.strip()

class Solution_3:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)
        
        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)
        

        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)
        
        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest) 
            elif not hundred and rest: 
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        if not num:
            return 'Zero'
        
        result = ''
        if billion:        
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''    
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result

abc = Solution_3()
print (abc.numberToWords(234567890))