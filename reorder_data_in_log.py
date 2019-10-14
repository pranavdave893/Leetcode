class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []
        for x in logs:
            if x[0] == 'l':
                letter_logs.append(x)
            else:
                digit_logs.append(x)
        letter_logs.sort(key=lambda x:(x[x.index(' ') + 1], x[:x.index(' ')]))
        return letter_logs + digit_logs

abc = Solution()
print (abc.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))