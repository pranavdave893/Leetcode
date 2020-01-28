class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        ans = []
        for rest in restaurants:
            if veganFriendly: 
                if rest[4] <= maxDistance and rest[2] == veganFriendly and rest[3] <= maxPrice:
                    ans.append(rest)
            else:
                if rest[4] <= maxDistance and rest[3] <= maxPrice:
                    ans.append(rest)
        
        ans = sorted(ans, key=lambda x : (x[1], x[0]), reverse=True)
        
        return [x[0] for x in ans]

abc = Solution()
print (abc.filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 1, 50, 10))

