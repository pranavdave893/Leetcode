class Solution:
    def numSteps(self, a,b,c):        
        abcd = [['a', a], ['b', b], ['c',c]]
        abcd.sort(key=lambda x: -x[1])
        
        ans = []
        
        for idx, x in enumerate(abcd):
            for y in range(abcd[idx][1]):
                ans.append(abcd[idx][0])
        
        start = 0
        end = len(ans)-1
        ct = 1
        while start < end:
            if start > 0 and ans[start] == ans[start-1]:
                ct += 1
            
            if ct == 3:
                if ans[start] != ans[end]:
                    ans[start], ans[end] = ans[end], ans[start]
                    end -= 1
                    ct = 1
            
            start += 1
        

        # if start+2 < len(ans):
        #     ans = ans[:start+2]
        # else:
        #     ans = ans[:start-1]
        ct = 1
        last = ans[len(ans)-1]
        first = True
            if ct < 3:
                if not first:
                    break
            for x in ans[::-1]:
                if x == last:
                    ct += 1
                
                if ct == 3:
                    ans.pop()

            first = False
            
        
        return "".join(ans)
     

abc = Solution()
print (abc.numSteps(2,2,1))
print (abc.numSteps(7,1,0))