class Solution(object):

    def simplify(self, path):
        stack = []

        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != ".":
                stack.append(p)
        
        print ("/" + "/".join(stack))

abc = Solution()
abc.simplify("/home//foo/")