class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        dct = {'(': 0, ')':0}

        lst = []        
        for x in s:
            if x == '(':
                dct[x] += 1
            if x == ')':
                if dct['('] <= 0:
                    continue
                dct['('] -= 1
            lst.append(x)
        
        dct = {'(': 0, ')':0}
        
        for y in range(len(lst)-1, -1, -1):
            temp = lst[y]
            if temp == ')':
                dct[temp] += 1
            if temp == '(':
                if dct[')'] <= 0:
                    lst[y] = "#"
                    continue
                dct[')'] -= 1
        
        ans = "".join([i for i in lst if i != "#"])

        return ans

abc = Solution()
print (abc.minRemoveToMakeValid("(a(b(c)d)"))
            