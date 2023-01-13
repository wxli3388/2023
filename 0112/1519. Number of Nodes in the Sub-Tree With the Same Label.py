class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        ans = [0 for _ in range(n)]
        self.dfs(ans, graph, labels, 0, -1)
        return ans
    def dfs(self, ans, graph, labels, root, parent):
        h = defaultdict(int)
        for nextOne in graph[root]:
            if nextOne!=parent:
                subH = self.dfs(ans, graph, labels, nextOne, root)
                for k in subH:
                    h[k]+=subH[k]
        h[labels[root]]+=1
        ans[root] = h[labels[root]]
        return h
        