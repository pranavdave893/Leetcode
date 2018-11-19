r,c = map(int,(input().split()))
a = [[0] * r for i in range(r)]
for i in range(r):
   for j in range(r):
        a[i][j] = int(input())

print (a)
col_r = 0
row_d = 0
col_l = -1
row_u = 0

i = 0
j = 0

def print_matrix(x,i,j):
    print (x[i][j], end=" ")

while(j<=c-col_r):
    for j in range(j,(c-col_r)):
        print_matrix(x,i,j)
    i+=1
    col_r+=1
    for i in range(i,(r-row_d)):
        print_matrix(x,i,j)
    row_d +=1
    j -= 1
    col = j
    for j in range(col,col_l,-1):
        print_matrix(x,i,j)
    col_l += 1
    i -=1
    row = i
    for i in range(row,row_u,-1):
        print_matrix(x,i,j)
    j +=1
    row_u += 1
    

