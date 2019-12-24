class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        deficit = 0
        gas_sum = 0
        start_point = 0
        
        for i in range(len(gas)):
            gas_sum = gas_sum + gas[i] - cost[i]
            if gas_sum < 0:
                deficit += gas_sum
                start_point = i+1
                gas_sum = 0
        
        if gas_sum + deficit >= 0:
            return start_point
        else:
            return -1

abc = Solution()
# [5,8,2,8]
# [6,5,6,6]
print (abc.canCompleteCircuit([5,8,2,8], [6,5,6,6]))
            


            

                



