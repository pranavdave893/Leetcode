"""
https://leetcode.com/problems/group-shifted-strings/
tags : Facebook, medium
"""
from typing import List
from collections import defaultdict

class Solution(object):
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for s in strings:
            key = ()
            
            for i in range(len(s) - 1):
                circular_difference = 26 + ord(s[i+1]) - ord(s[i])
                key += (circular_difference%26,)
            hashmap[key].append(s)
        
        print(list(hashmap.values()))

abc = Solution()
abc.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "ab", "a", "z"])