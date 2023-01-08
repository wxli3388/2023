class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 0 => 1 => -2
        # 1 => 0 => -4
        # 2 => -1 => -6
        # 3 => -2 => -3
        # 4 => 2 => 0
        cnt = 0
        minVal = 9999
        index = 0
        for i in range(len(gas)):
            cnt = cnt+gas[i]-cost[i]
            if cnt<minVal:
                minVal = cnt
                index = i+1
        if cnt<0:
            return -1
        return index%len(gas)