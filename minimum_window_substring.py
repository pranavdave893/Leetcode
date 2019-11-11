from collections import Counter
class Solution(object):
    def minWindow(self, search_string, target):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        cnt = Counter(target)
        start = 0
        end = 0
        target_length = len(target)
        min_window = ""

        for end in range(len(search_string)):
            if cnt[search_string[end]] > 0:
                target_length -= 1
            
            cnt[search_string[end]] -= 1

            while target_length == 0:
                window_length = end - start + 1
                if not min_window or window_length < len(min_window):
                    min_window = search_string[start:end+1]

                cnt[search_string[start]] += 1

                if cnt[search_string[start]] > 0:
                    target_length += 1
                
                start += 1
        
        print(min_window)

abc = Solution()
abc.minWindow("AABABCC","ABC")