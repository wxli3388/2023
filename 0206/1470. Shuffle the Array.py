class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        for i in range(n):
            ans[2*i] = nums[i]
            ans[2*i+1] = nums[i+n]
        return ans
            