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
            
            for i in xrange(len(s)):
                if s[i] in {'(', ')'}:
                    new_s = s[:i] + s[i+1:]
                    new_s_count = find_positive_negative_count(new_s)
                    if new_s not in self.visited and new_s_count < curr_count:
                        self.visited.add(new_s)
                        dfs(new_s, new_s_count, res)
        
        dfs(s, find_positive_negative_count(s), res)
        return res

    def removeInvalidParentheses_bfs(self, s):
        def is_valid(s):
            ctr = 0
            for x in s:
                if x == '(':
                    ctr += 1
                elif x == ')':
                    ctr -= 1
                elif ctr < 0:
                    return False

            return ctr == 0

        q = {s}

        result = []
        while q:
            for x in q:
                if is_valid(s):
                    result.append(x)
            if result:
                return result
            
            new_q = set()
            for x in q:
                for i in xrange(len(x)):
                    new_s = x[:i] + x[i+1:]
                    new_q.add(new_s)
            q = new_q
        
        return [""]


abc = Solution()
print (abc.removeInvalidParentheses_bfs("()())()"))