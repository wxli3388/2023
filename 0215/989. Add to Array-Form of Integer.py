class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        cur = 0
        for i in num:
            cur = cur*10+i
        cur+=k
        ans = []
        while cur>0:
            ans.append(cur%10)
            cur//=10
        return ans[::-1]