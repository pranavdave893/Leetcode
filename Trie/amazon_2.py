"""
maxTravelDist = 7000
forwardRouteList = [[1,2000],[2,4000],[3,6000]]
returnRouteList = [[1,2000]]

output:
[[2,1]]

maxTravelDist = 10000
forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]]
returnRouteList = [[1,2000],[2.3000],[3,4000],[4,5000]]

output:
[[2,4],[3,2]]
"""
maxTravelDist = 10000
forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]]
returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]

best_dist = []
i = len(forwardRouteList) - 1
j = 0
best_sum = 0

while j<=len(returnRouteList)-1 and i >= 0:
    dist_sum =  forwardRouteList[i][1] + returnRouteList[j][1]

    if dist_sum <= maxTravelDist:
        
        if dist_sum > best_sum:
            best_dist = []
            best_dist.append([forwardRouteList[i][0],returnRouteList[j][0]])
            best_sum = dist_sum
        
        elif dist_sum == best_sum:
            best_dist.append([forwardRouteList[i][0],returnRouteList[j][0]])
        
        j += 1
    
    else:
        i -= 1

print (best_dist)
        








    
    