class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ns, ne = newInterval
        if ne<intervals[0][0]:
            return [newInterval]+intervals
        if ns>intervals[-1][1]:
            return intervals+[newInterval]
        
        ans = []
        for index in range(len(intervals)):
            s, e = intervals[index]
            if e<newInterval[0]:
                ans.append([s,e])
            elif s>newInterval[1]:
                return ans+[newInterval]+intervals[index:]
            else:
                newInterval[0] = min(newInterval[0], s)
                newInterval[1] = max(newInterval[1], e)
        ans.append(newInterval)
        return ans