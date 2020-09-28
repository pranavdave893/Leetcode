def is_dollar_delete_equal(arr):
    # fill in
    for word in arr:
      start, end = 0, len(word)
      while start < end:
        if word[start] == "$":
          word = word[:start-1] + word[start+1:] 
          end = len(word)
          continue
        start += 1
    
    print (set(arr))
    return len(set(arr)) <=1 

print (is_dollar_delete_equal(['a90$n$c$se', 'a90n$cse']))