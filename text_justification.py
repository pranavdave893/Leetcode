class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        ans = []

        temp = []
        curr_len = 0
        is_first = is_last = True
        x = 0
        while x < len(words):
            if curr_len + len(words[x]) + 1 <= maxWidth:
                if not is_first:
                    temp.append(" ")
                    curr_len += 1
                
                is_first = False
                temp.append(words[x])
                if temp:
                    curr_len += len(temp[-1])
                x += 1
            elif not temp and len(words[x]) == maxWidth:
                temp.append(words[x])
                curr_len = len(words[x])
                remaining_len = 0
                x += 1
            else:
                remaining_len = maxWidth - curr_len
                
                new_temp = []
                curr_space = " "
                while remaining_len:
                    if len(temp) == 1:
                        new_temp.append(temp[-1])
                        while remaining_len:
                            new_temp.append(" ")
                            remaining_len -= 1
                        temp = new_temp
                        break
                    else:                    
                        for j in temp:
                            if remaining_len and j == curr_space:
                                new_temp.append(j + " ")
                                remaining_len -= 1
                            else:
                                new_temp.append(j)

                        temp = new_temp
                        new_temp = []
                        curr_space += " "

                ans.append(''.join(temp))
                temp = []
                curr_len = 0
                is_first = True
        
        if temp:
            remaining_len = maxWidth - curr_len
            while remaining_len:
                temp.append(" ")
                remaining_len -= 1
        
        ans.append(''.join(temp))

            
        return ans

abc = Solution()
abc.fullJustify(["Listen","to","many,","speak","to","a","few."], 6)
