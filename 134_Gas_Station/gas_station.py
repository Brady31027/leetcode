class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        size = len(gas)
        start, gas_left = 0, 0
        for i in range(size):
            gas_left += (gas[i] - cost[i])
            if gas_left < 0:
                start = i + 1
                gas_left = 0
        return start if sum(gas) >= sum(cost) else -1
            
            
        
