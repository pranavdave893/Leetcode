class Solution(object):

    def removeInvalidParentheses(self, s):
        res = []
        self.visited = set([s])

        def find_positive_negative_count(s):
            """
            Returns sum of 'misplaced' parenthesis.
            """
            plus = minus = 0
            for x in s:
                plus += {'(': 1, ')': -1}.get(x, 0)
                if plus < 0:
                    minus += 1
        
                plus = 0 if plus < 0 else plus
            
            return plus + minus

        def dfs(s, curr_count, res):
            if curr_count == 0:
                res.append(s)
                return
            
            for i in range(len(s)):
                if s[i] in {'(', ')'}:
                    new_s = s[:i] + s[i+1:]
                    new_s_count = find_positive_negative_count(new_s)
                    if new_s not in self.visited and new_s_count < curr_count:
                        self.visited.add(new_s)
                        dfs(new_s, new_s_count, res)
        
        dfs(s, find_positive_negative_count(s), res)
        return res
    
    def is_valid(self, s):
        count = 0
        for x in s:
            count += 1 if x == "(" else 0
            count -= 1 if x == ")" else 0
            if count < 0:
                return False
        return count == 0

    def removeInvalidParentheses_bfs(self, s):
        level = {s}
        while True:
            new_level = set()
            result = []

            for x in level:
                if self.is_valid(x):
                    result.append(x)

            if result: return result
        
            for x in level:
                for i in range(len(x)):
                    new_level.add(x[:i] + x[i+1:])
            level = new_level


abc = Solution()
print (abc.removeInvalidParentheses("()())()"))