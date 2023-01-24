class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        count = [0]*(n+1)
        isJudgeTrust = [0]*(n+1)
        maxOne = 0
        maxIndex = -1
        for s, e in trust:
            count[e]+=1
            if count[e]>maxOne:
                maxOne = count[e]
                maxIndex = e
            isJudgeTrust[s] = True
        if maxOne==n-1 and not isJudgeTrust[maxIndex]:
            return maxIndex
        return -1

