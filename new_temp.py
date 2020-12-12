def smallest_string(n, k):
    ans = ['a']*n  # Initialize the answer to be 'aaa'.. length n
    val = n           #Value would be length as all are 'a'
    
    for i in range(n-1, -1, -1):    
        if val == k:           # if value has reached k, we have created our lexicographically smallest string
            break
        val -= 1                # reduce value by one as we are removing 'a' and replacing by a suitable character
        ans[i] = chr(96 + min(k - val, 26))   # replace with a character which is k - value or 'z'
        val += ord(ans[i]) - 96                     # add the value of newly appended character to value
        
    return ''.join(ans) 

print (smallest_string(5, 73))