class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        return max(self.dfs(0, -1, graph, hasApple)-2, 0)
    def dfs(self, node, parent, graph, hasApple):

        res = 0
        for nextOne in graph[node]:
            if nextOne!=parent:
                res+=self.dfs(nextOne, node, graph, hasApple)
        if res or hasApple[node]:
            return res+2
        return res