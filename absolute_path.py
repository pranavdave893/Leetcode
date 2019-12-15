class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Splitting is O(n*m) - where m is the length of the character to split, here this is O(n)
        plist = path.split('/')
        stack = []
        for directory in plist:
            if directory == "." or not directory:
                continue
            # Need this condition nested for case of /../a
            elif directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
        return "/" + "/".join(stack)

abc = Solution()
print (abc.simplifyPath("/a//b////c/d//././/.."))