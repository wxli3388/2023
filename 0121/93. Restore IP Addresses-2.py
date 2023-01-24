class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(0, s, [], ans)
        return ans
    
    def dfs(self, index, s, cur, ans):
        if len(cur)>4:
            return
        if index==len(s):
            if len(cur)==4:
                ans.append(".".join(cur))
            return
        for i in range(index, len(s)):
            if index-i==3:
                return
            temp = s[index:i+1]
            if (temp[0]=="0" and len(temp)==1 or temp[0]!="0") and 0<=int(temp)<=255:
                cur.append(temp)
                self.dfs(i+1, s, cur, ans)
                cur.pop()