class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        h = Counter(tasks)
        ans = 0
        for k in h:
            if h[k]==1:
                return -1
            if h[k]%3==0:
                ans+=h[k]//3
            else:
                ans+=h[k]//3+1
        return ans