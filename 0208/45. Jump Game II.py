class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        curFarthest = 0
        curEnd = 0
        for i in range(len(nums)-1):
            curFarthest = max(curFarthest, i+nums[i])
            if i==curEnd:
                curEnd = curFarthest
                ans+=1
        return ans