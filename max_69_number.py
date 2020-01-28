class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        list_words = s.split()
        
        
        max_length = 0
        
        for word in list_words:
            max_length = max(len(word), max_length)
            
        i,j = 0,0 
        
        ans = []
        while i < max_length:
            j = 0
            temp = []
            while j < len(list_words):

                if i >= len(list_words[j]):
                    temp.append(" ")
                else:
                    temp.append(list_words[j][i])
                
                j += 1
            ans.append(''.join(temp).rstrip())
            
            i += 1
        
        return ans

abc = Solution()
print (abc.printVertically("TO BE OR NOT TO BE"))
print (abc.printVertically("CONTEST IS COMING"))