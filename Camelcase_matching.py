class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        
        for query in queries:
            i = 0
            pt_ptr = 0
            while i < len(query)-1: 
                if query[i].isupper() and query[i] == pattern[pt_ptr]:
                    i+=1
                    pt_ptr+=1
                elif query[i].islower():
                    i+=1
                    continue
                else:
                    
                    
