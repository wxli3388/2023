class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # (y1-y2)/(x1-x2) = (y3-y1)/(x3-x1)
        # => (y1-y2)*(x3-x1) = (y3-y1)*(x1-x2)
        ans = 1
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                same = 2
                for k in range(j+1, len(points)):
                    x3, y3 = points[k]
                    if (y1-y2)*(x3-x1) == (y3-y1)*(x1-x2):
                        same+=1
                ans = max(same, ans)
        return ans

        