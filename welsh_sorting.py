alphabets = ['a','b','c','ch','dd','d','e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
alpha_index = {}
for idx,val in enumerate(alphabets):
    alpha_index[val] = idx

def comp(s):
    temp = []
    i = 0
    while i < len(s)-1:
        if s[i] + s[i+1] in alpha_index.keys():
            temp.append(alpha_index[s[i] + s[i+1]])
            i+=2
        else:
            temp.append(alpha_index[s[i]])
            i += 1
    temp.append(alpha_index[s[len(s)-1]])
    return tuple(temp)

strings = ['abcchd', 'abcdd']
a = strings.sort(key=comp)
print(strings)