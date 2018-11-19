
x = {
    '{':'}',
    '(':')',
    '[':']',
}
flag = False
stack = []
strc = input()
for i in strc:
    if len(strc) %2 !=0:
        break
    if i in x.keys():
        stack.append(i)
    elif i in x.values():
        if len(stack)<1:
            flag = False
            break
        j = stack.pop()
        if x[j] == i:
            flag = True
        else:
            flag = False
            break
if flag:
    print('balanced')
else:
    print('not balanced')
