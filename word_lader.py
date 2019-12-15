from collections import defaultdict
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        https://leetcode.com/problems/word-ladder/discuss/346920/Python3-Breadth-first-search
        """
        word_map = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
               new_word = word[:i] + "*" + word[i+1:]
               word_map[new_word].append(word)
        
        answer = []
        q = deque([(beginWord, 1)])
        visited = set()
        tmp_answer = [beginWord]
        def find_path(tmp_answer, word_map, visited, currWord):
            for i in range(L):
                # check for word like h*t, *ot in word_map
                for new_possible_word in word_map[currWord[:i] + "*" + currWord[i+1:]]:
                    if new_possible_word == endWord:
                        tmp_answer.append(endWord)
                        return tmp_answer
                    
                    if new_possible_word not in visited:
                        tmp_answer.append(new_possible_word)
                        visited.add(new_possible_word)
                        
                        find_path(tmp_answer, word_map, visited, new_possible_word)
            return []
        
        
        tmp_list = find_path(tmp_answer, word_map, visited, beginWord)
        if tmp_list:
            answer.append(tmp_list)
        return answer


    def ladderLength_bi_bfs(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict: return 0
        word_map = defaultdict(list)
        L = len(beginWord)
        level = 0
        for word in wordList:
            for i in range(L):
               new_word = word[:i] + "*" + word[i+1:]
               word_map[new_word].append(word)
        

        forward = {beginWord}
        backward = {endWord}
        wordDict.remove(endWord)

        while forward and backward:
            level += 1
            new_set = set()

            if len(forward) > len(backward): forward, backward = backward, forward

            for currWord in forward:
                newWords = []
                for x in range(L):
                    for new_word in word_map[currWord[:x] + "*" + currWord[x+1:]]:
                        newWords.append(new_word)
                
                for newWord in newWords:
                    if newWord in backward: return level + 1
                    if newWord not in wordDict: continue
                    wordDict.remove(newWord)
                    new_set.add(newWord)
            forward = new_set
        
        return 0

abc = Solution()
print (abc.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))