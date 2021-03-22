def trapping(arr):
    i = 0
    n = len(arr)
    j = n - 1

    ans = 0
    left_max = 0
    right_max = 0

    while i < j:

        if arr[i] < arr[j]:
            if arr[i] < left_max:
                left_max = arr[i]
            
            else:
                ans += (left_max - arr[i])

            
            i += 1
        
        else:
            

            



