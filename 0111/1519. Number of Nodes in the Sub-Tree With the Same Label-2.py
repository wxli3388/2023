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
        count = [0 for _ in range(26)]
        for nextOne in graph[root]:
            if nextOne!=parent:
                subCount = self.dfs(ans, graph, labels, nextOne, root)
                for idx in range(26):
                    count[idx]+=subCount[idx]
        index = ord(labels[root])-97 
        count[index]+=1
        ans[root] = count[index]
        return count