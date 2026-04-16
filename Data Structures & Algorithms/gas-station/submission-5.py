class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:

        if sum(gas) < sum(cost):
            return -1

        # FIND THE START STATION
        total = 0
        start = 0
        for i in range(len(gas) - 1):
            total += gas[i] - cost[i]
            if total < 0: # if total is negative, we cannot complete the circuit
                total = 0
                start = i + 1
        return start
                
