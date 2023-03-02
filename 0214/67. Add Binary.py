class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a)-1
        j = len(b)-1
        ans = ""
        while i>=0 or j>=0:
            n1, n2 = 0, 0
            if i>=0:
                n1 = int(a[i])
                i-=1
            if j>=0:
                n2 = int(b[j])
                j-=1
            total = n1+n2+carry
            if total>=2:
                carry = 1
            else:
                carry = 0
            total%=2
            ans = str(total)+ans
        if carry>0:
            ans = str(carry)+ans
        return ans
            
            