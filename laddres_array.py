
T = int(input())
while(T !=0):
    N = int(input())
    a = list(map(int,input().strip(' ').split(' ')))
    # a = [16,17,4,3,5,2]
    x = len(a)-1
    ans = []
    mx = a[x]
    ans.append(a[x])
    while(x !=0 ):
        if a[x-1] > mx:
            mx = a[x-1]
            ans.append(mx)
        x = x-1
    print (*ans[::-1])
    T = T -1 



        
            