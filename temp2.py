def decreasing_price(nums):
    pre = float('inf')
    ans = 0
    mx_ans=0
    for x in nums:
        if x < pre:
            ans += 1
            mx_ans = max(ans, mx_ans)
            pre = x
        elif x == pre:
            continue
        else:
            pre = x
            ans = 0
    return mx_ans

print (decreasing_price([3,2,2,1]))
