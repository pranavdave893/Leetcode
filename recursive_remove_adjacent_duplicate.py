class Solution():

    def remove_duplicate(self, s):
        if len(s) <= 1:
            return s

        start, end = 0, 1

        while end < len(s):
            if s[end] == s[start]:
                while end < len(s) and s[end] == s[start]:
                    end += 1
                
                return self.remove_duplicate(s[:start]+s[end:])
            else:
                end += 1
                start += 1
        
        return s

abc = Solution()
print (abc.remove_duplicate("azxxzy"))
print (abc.remove_duplicate("geeksforgeeg"))
print (abc.remove_duplicate("acaaabbbacdddd"))

        
