a = "rellnmpapqfwkhop"
b = "llnmpapqfwkhopre"
c = "onamaz"
temp = a[0]+a[1]
temp2 = a[len(a)-2] + a[len(a)-1]
print temp,temp2
if temp == b[-2:] or temp2 == b[:2]:
    print 1
else:
    print 0