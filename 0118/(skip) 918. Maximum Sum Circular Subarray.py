class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        maxSum = nums[0]
        curMin = 0
        minSum = nums[0]

        total = 0
        for n in nums:
            curMax = max(curMax+n, n)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin+n, n)
            minSum = min(minSum, curMin)
            total+=n
        
        if maxSum>0:
            return max(maxSum, total-minSum)
        return maxSum
