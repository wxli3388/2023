class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        h = [0 for _ in range(26)]
        for c in p:
            h[ord(c)-97]+=1
        ans = []
        pre = 0
        current = [0 for _ in range(26)]
        for i in range(len(s)):
            current[ord(s[i])-97]+=1
            if i>=len(p):
                current[ord(s[pre])-97]-=1
                pre+=1
            if current==h:
                ans.append(i-len(p)+1)
        return ans