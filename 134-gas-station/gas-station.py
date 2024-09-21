class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff, sol, s = [], [], 0
        if sum(cost) > sum(gas):
            return -1

        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        
        for i in range(len(gas)-1, -1, -1):
            s += diff[i]
            sol.append(s)

        pos = sol.index(max(sol))
        return len(gas) -1 - pos 

        