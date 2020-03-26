class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        num_to_eng_dict = {
            0:'zero',1: 'One', 2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',
            8:'Eight', 9:'Nine', 10:'Ten', 11: 'Eleven', 12: 'Twelve', 13:'Thriteen', 14:'Fourteen',
            15:'Fifteen', 16:'Sixteen', 17:'Seventeen',18:'Eighteen', 19: 'Nineteen', 20:'Twenty', 
            30:'Thrity', 40:'Fourty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80: 'Eighty', 
            90:'Ninty',
        }

        str_num = str(num)

        def recur(num):
            if num == 0:
                return ''

            if num <= 20:
                return num_to_eng_dict[num]
            
            if 20 < num < 100:
                abc = (num // 10) * 10
                ans = num_to_eng_dict[abc] + recur(num % 10)
                return ans
            
            elif 20 < num < 999:
                abc = num // 100 
                ans = num_to_eng_dict[abc] + " Hundred " + recur(num % 100)
                return ans
            
            elif 1000 <= num < 99999:
                abc = num // 1000
                ans = num_to_eng_dict[abc] + " Thousand " + recur(num % 1000)
                return ans



        ans = recur(num)
        return ans

abc = Solution()
print (abc.numberToWords(10000))




            
            

