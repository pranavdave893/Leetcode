class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        
        if len(chars) == 1:
            return 1
        
        first, second = 0, 1
        
        while first < len(chars) and second < len(chars):

            ct = 1
            while second < len(chars) and chars[first] == chars[second]:
                ct += 1
                second += 1

            if ct > 1:
                if chars[:first]:
                    chars = chars[:first] + chars[second-1:second] + [x for x in str(ct)] + chars[second:]
                else:
                    chars = chars[second-1:second] + [x for x in str(ct)] + chars[second:]

            first = second
            second += 1
            
        
        print (chars) 

abc = Solution()
abc.compress(["a"])