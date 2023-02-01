class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1)>len(str2):
            str1, str2 = str2, str1
        ans = ""
        for i in range(1, len(str1)):
            prefix = str1[:i]
            if len(str1)%len(prefix)==0 and len(str2)%len(prefix)==0:
                notSame1 = False
                for j in range(0, len(str1), len(prefix)):
                    if str1[j:j+len(prefix)]!=prefix:
                        notSame1 = True
                        break
                notSame2 = False
                for j in range(0, len(str2), len(prefix)):
                    if str2[j:j+len(prefix)]!=prefix:
                        notSame2 = True
                        break
                
                if not notSame1 and not notSame2:
                    ans = prefix
        return ans
                    