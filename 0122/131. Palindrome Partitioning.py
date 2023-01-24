class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.dfs(0, s, [], ans)
        return ans
    def dfs(self, index, s, cur, ans):
        if index==len(s):
            ans.append(cur[:])
            return
        for i in range(index, len(s)):
            temp = s[index:i+1]
            if self.isPalindrome(temp):
                cur.append(temp)
                self.dfs(i+1, s, cur, ans)
                cur.pop()

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i, j = i+1, j-1
        return True