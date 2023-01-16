class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
        for index in range(len(s1)):
            self.union(ord(s1[index])-97, ord(s2[index])-97, parent)
        ans = ""
        for c in baseStr:
            index = ord(c)-97
            ans+=chr(self.find(index, parent)+97)
        return ans
    def union(self, i, j, parent):
        root_i, root_j = self.find(i, parent), self.find(j, parent)
        if root_i==root_j:
            return
        if root_i<root_j:
            parent[root_j] = root_i
        else:
            parent[root_i] = root_j
    def find(self, i, parent):
        if parent[i]!=parent[parent[i]]:
            parent[i] = self.find(parent[parent[i]], parent)
        return parent[i]