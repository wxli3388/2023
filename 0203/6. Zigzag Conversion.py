class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = [[] for _ in range(numRows)]
        offset = 1
        rowIndex = 0
        for i in range(len(s)):
            row[rowIndex].append(s[i])
            if rowIndex+1==len(row):
                offset = -1
            elif rowIndex-1<0:
                offset = 1
            rowIndex+=offset
        ans = ""
        for arr in row:
            ans+="".join(arr)
        return ans