class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(s, 0, "", [], ans)
        return ans
    
    def dfs(self, s, index, curPart, cur, ans):
        if index==len(s):
            if len(cur)==3 and int(curPart)>255:
                return
            if curPart!="":
                cur.append(curPart)
            if len(cur)==4:
                ans.append(".".join(cur))
            return
        if curPart=="":
            self.dfs(s, index+1, curPart+s[index], cur, ans)
            return
        if len(curPart)==3:
            if(int(curPart)>255):
                return
            cur.append(curPart)
            self.dfs(s, index, "", cur, ans)
            cur.pop()
            return
        self.dfs(s, index, "", cur+[curPart], ans)
        if curPart[0]!="0":
            self.dfs(s, index+1, curPart+s[index], cur, ans)