class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        hold = prices[0]
        for i in prices:
            ans = max(ans, i-hold)
            hold = min(hold, i)
        return ans