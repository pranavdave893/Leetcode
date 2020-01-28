from collections import defaultdict, deque
class Solution(object):
    def wordLader(self, beginWord, endWord, wordList):
        # wordList = set(wordList)
        
        word_map = defaultdict(list)
        L = len(beginWord)

        if endWord not in wordList:
            return 0
        
        for word in wordList:
            for i in range(L):
                word_map[word].append([word[:i] + "*" + word[i+1:]])
        
        dq = deque([(beginWord, 1)])
        visited = set()

        ans = []
        tmp_1 = tmp_2 = [beginWord]
        is_true = False
        is_second = False
        while dq:
            current, level = dq.popleft()
            

            for i in range(L):
                for new_word in word_map[[current[:i] + "*" + current[i+1:]]]:
                    if new_word == endWord:
                        is_true = True
                        tmp_1.append(endWord)
                        tmp_2.append(endWord)
                        break

                    if new_word not in visited:
                        if is_second:
                            tmp_2.append(new_word)
                            is_second = False
                        else:
                            tmp_1.append(new_word)
                            is_second = True

                        visited.add(new_word)
                        dq.append((new_word, level+1))

                if is_true:
                    
                    break
        
        return 0

abc = Solution()
print (abc.wordLader("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
                

        
