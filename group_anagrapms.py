class Solution(object):
    def groupAnagrams(self, strs):
        """
        
        Arguments:
            object {[type]} -- [description]
            strs {[type]} -- [description]
        """
        abc = {}

        for s in strs:
            x = tuple(sorted(s))
            if x not in abc:
                abc[x] = [s]
            else:
                abc[x].append(s)
        
        print([abc[i] for i in abc])


ip = ["eat", "tea", "tan", "ate", "nat", "bat"]
abc = Solution()
abc.groupAnagrams(ip)

