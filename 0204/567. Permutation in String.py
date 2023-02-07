class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h = [0 for _ in range(26)]
        for c in s1:
            h[ord(c)-97]+=1
        current = [0 for _ in range(26)]
        pre = 0
        for i in range(len(s2)):
            if i>=len(s1):
                current[ord(s2[pre])-97]-=1
                pre+=1
            current[ord(s2[i])-97]+=1
            if current==h:
                return True
        return False