class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        cur = 0
        h = defaultdict(int)
        h[0] = 1
        for n in nums:
            cur = (cur+n)%k
            ans+=h[cur]
            h[cur]+=1
        return ans