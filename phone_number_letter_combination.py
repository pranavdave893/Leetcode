class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2':'abc', '3':'def' }

        def phoneMapping(rst, remaining_digits):
            if len(remaining_digits) == 0:
                return rst
            
            if len(rst) == 0:
                rst = ['']
            
            digit = remaining_digits.pop(0)
            nxt_rst = []
            
            for r in rst:
                for c in mapping[digit]:
                    nxt_rst.append(r+c)
            
            return phoneMapping(nxt_rst, remaining_digits)

        return phoneMapping([], list(digits))

abc = Solution()
print (abc.letterCombinations('23'))