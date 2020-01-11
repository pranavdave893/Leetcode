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
        # wordList = set(wordList)
        
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)

        word_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                word_dict[word[:i] + "*" + word[i+1:]].append(word)
        
        dq = deque([(beginWord, 1)])
        visited = set()
        tmp = []

        while dq:
            current_word, level = dq.popleft()
            for i in range(L):
                for new_word in word_dict[current_word[:i] + "*" + current_word[i+1:]]:
                    tmp.append(new_word)
                    if new_word == endWord:
                        return tmp, level + 1
                
                    if new_word not in visited:
                        visited.add(new_word)
                        dq.append((new_word, level+1))
        
        return 0
        
        
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