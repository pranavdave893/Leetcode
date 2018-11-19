prices = [1,2,3,4,5,6]
prices = [7,1,5,3,6,4]
sell = 0
profit = 0
buy = prices[0]
bought = False
for p in prices:
    if p < buy:
        buy = p
    else:
        profit += p - buy
        buy = p
print profit