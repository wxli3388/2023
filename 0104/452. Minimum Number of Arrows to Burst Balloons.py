class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 1
        preMax = points[0][1]
        for i in range(1, len(points)):
            if points[i][0]>preMax:
                ans+=1
                preMax = points[i][1]
            elif points[i][1]<preMax:
                preMax = points[i][1]
        return ans