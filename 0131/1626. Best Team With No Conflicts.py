class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = sorted(zip(ages, scores))
        dp = [[-1 for _ in range(len(scores))] for _ in range(len(scores))]
        return self.findMax(-1, 0, arr, dp)
    def findMax(self, prev, index, arr, dp):
        if index==len(arr):
            return 0
        if dp[prev+1][index]!=-1:
            return dp[prev+1][index]
        if prev==-1 or arr[prev][1]<=arr[index][1]:
            value = max(self.findMax(prev, index+1, arr, dp), arr[index][1]+self.findMax(index, index+1, arr, dp))
        else:
            value = self.findMax(prev, index+1, arr, dp)
        dp[prev+1][index] = value
        return dp[prev+1][index]