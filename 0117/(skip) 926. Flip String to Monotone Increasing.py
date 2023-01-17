class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        one = 0
        flip = 0
        for index in range(len(s)):
            if s[index]=="0":
                if one==0:
                    continue
                flip+=1
            else:
                one+=1
            if flip>one:
                flip = one
        return flip