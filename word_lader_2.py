from collections import defaultdict
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        
        graph = defaultdict(set)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                graph[word[:i] + '_' + word[i + 1:]].add(word)
        wordList = set(wordList)
        
        queue = [[beginWord]]
        flag = False
        while queue:
            
            new_queue = []
            to_remove = set()

            for path in queue:
                for i in range(L):
                    for new_word in path[-1][:i] + "*" + path[-1][i+1:]:
                        if new_word in wordList:
                            new_queue = path + [new_word]
                            to_remove.add(new_word)
                        
                        if new_word == endWord:
                            






abc = Solution()
print (abc.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))