"""
Hacker rank OA 
company : Riot Games

"""
# function 
def printGardenLayout():
    
    width = 0
    height = 0
    s = input("input should be comma separeted width & height of matrix ( like 10,10 ) \n") # input a string
    lst = s.split(',') # split width and height
    width = int(lst[0]) # get width
    height = int(lst[1]) # get height

    row, col = (width, height) # create 2D-Array ( Matrix )
    gardan = [['B' for i in range(col)] for j in range(row)]

    while True:
        s = input(f"input should be between 0-{width} ( put 0 to exit ) : ")
        if not s:
            break
        else:
            x = int(s)
            y = int(s)
            gardan[x][y] = s
        


    for r in gardan: 
        print(r)

printGardenLayout()