class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for node in range(1, len(parent)):
            graph[parent[node]].append(node)
        self.ans = 1
        self.dfs(graph, 0, s)
        return self.ans
    def dfs(self, graph, root, s):
        
        max1 = max2 = 0        
        for nextNode in graph[root]:
            length = self.dfs(graph, nextNode, s)
            if s[nextNode]!=s[root]:
                if length>=max1:
                    max1, max2 = length, max1
                elif length>max2:
                    max2 = length
        self.ans = max(self.ans, max1+max2+1)
        return max1+1