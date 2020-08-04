from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        start = beginWord
        end = endWord
        
        word_set = set(wordList)
        n = len(start)
        
        graph = defaultdict(list)
        
        for word in word_set:
            for x in range(n):
                graph[word[:x] + "*" + word[x+1:]].append(word)
        
        
        
        q = [[start]]
        flag = False
        while q:
            new_q = []
            
            to_remove = set()
            
            for word in q:
                for i in range(n):
                    for new_word in graph[word[-1][:i] + "*" + word[-1][i+1:]]:
                        if new_word in word_set:
                            new_q.append(word + [new_word])
                            to_remove.add(new_word)
                            
                            if new_word == end:
                                flag = True
                            
            if flag:
                return [p for p in new_q if p[-1] == end]
            
            q = new_q[:]
            word_set -= to_remove
        
        return []

        # graph = defaultdict(set)
        # for word in wordList:
        #     for i in range(len(word)):
        #         graph[word[:i] + '_' + word[i + 1:]].add(word)
        # wordList = set(wordList)
        
        # queue = [[beginWord]]

        # flag = False
        
        # while queue:
        #     new_queue = []
        #     to_remove = set()
        
        #     for path in queue:
                
        #         for i in range(len(path[-1])):
                    
        #             for new_word in graph[path[-1][:i] + '_' + path[-1][i + 1:]]:
        #                 if new_word in wordList:
        #                     new_queue.append(path + [new_word])
        #                     to_remove.add(new_word)
        #                     if new_word == endWord: flag = True
            
        #     if flag: return [p for p in new_queue if p[-1] == endWord]
        #     queue = new_queue[:]
        #     wordList -= to_remove
        # return []

abc = Solution()
print (abc.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))