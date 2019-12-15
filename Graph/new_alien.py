class Solution(object):
    def alienOrder(self, words):
        graph = {}
        for word in words:
            for char in word:
				if char not in graph:
					graph[char] = []
        print (graph)

        def addEdge(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
				char1 = word1[i]
				char2 = word2[i]
				if char1 != char2:
					if char2 not in graph[char1]:
						graph[char1].append(char2)
					break
				i += 1

        for i in range(len(words)-1):
			word1 = words[i]
			word2 = words[i+1]

			addEdge(word1, word2)

        print (graph)

abc = Solution()
abc.alienOrder(["z","y","x","c","y","b"])