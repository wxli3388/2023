class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        self.dfs(nums, 0, [], ans)
        return ans
    def dfs(self, nums, index, cur, ans):
        if len(cur)>1:
            # ans.append(cur[:])
            ans.add(tuple(cur))
        if index==len(nums):
            return 
        for i in range(index, len(nums)):
            if len(cur)==0 or nums[i]>=cur[-1]: 
                cur.append(nums[i])
                self.dfs(nums, i+1, cur, ans)
                cur.pop()
