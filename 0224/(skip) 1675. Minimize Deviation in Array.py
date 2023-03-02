class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minValue = math.inf
        ans = math.inf
        maxH = []
        for i in range(len(nums)):
            if nums[i]%2==1:
                nums[i]*=2
            minValue = min(minValue, nums[i])
            maxH.append(-nums[i])
        heapq.heapify(maxH)
        while maxH:
            value = -heapq.heappop(maxH)
            ans = min(ans, abs(value-minValue))
            if value%2==1:
                break
            minValue = min(minValue, value//2)
            heapq.heappush(maxH, -(value//2))
        return ans
            