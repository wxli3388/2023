class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        h = defaultdict(int)
        pre = 0
        cnt = 0
        ans = 0
        for i in range(len(fruits)):
            h[fruits[i]]+=1
            cnt+=1
            while len(h)>2:
                h[fruits[pre]]-=1
                if h[fruits[pre]]==0:
                    del h[fruits[pre]]
                pre+=1
                cnt-=1
            ans = max(ans, cnt)
        return ans
                