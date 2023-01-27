class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        ans = []
        for word in words:
            if self.dfs(word, s, ans):
                ans.append(word)
        return ans
    def dfs(self, word, s, ans):
        for i in range(1, len(word)):
            first = word[:i]
            second = word[i:]
            if first in s:
                if second in s:
                    return True
                if self.dfs(second, s, ans):
                    return True
        return False
