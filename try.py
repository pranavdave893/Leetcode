t = int(input())
while(t != 0):
    mx_sum = 0
    x = int(input().strip(' '))
    if (x <10):
        print (x)
        t = t - 1
        continue
    while(x != 0):
        y = x % 10
        x = x // 10
        mx_sum = mx_sum + y

    while(mx_sum != 0):
        a = mx_sum % 10
        new_sum = mx_sum // 10
        mx_sum = a + new_sum
        if mx_sum < 10:
            print (new_sum*a)
            break
    t = t - 1

