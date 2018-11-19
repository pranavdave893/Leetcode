class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        idx = len(digits)-1
        digits[idx]+= 1
        
        while True:
            if digits[idx] > 9:
                digits[idx] = 0
                if idx == 0:
                    if digits[idx] == 9:
                        digits[idx] = 0
                        digits.append(1)
                        return digits[::-1]
                    elif digits[0] == 0:
                        digits.append(1)
                        return digits[::-1]
                    
                digits[idx-1] += 1
                idx = idx - 1
            else:
                return digits

abc = Solution()
print abc.plusOne([9,8,7,9])