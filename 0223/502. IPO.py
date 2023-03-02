class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        project = sorted(zip(capital, profits))
        ptr = 0
        q = []
        for i in range(k):
            while ptr<len(project) and w>=project[ptr][0]:
                heappush(q, -project[ptr][1])
                ptr+=1
            if not q:
                break
            w+=-heappop(q)
        return w