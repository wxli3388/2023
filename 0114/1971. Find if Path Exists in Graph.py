class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        graph = defaultdict(list)
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
        visited = [False for _ in range(n)]
        q = deque([source])
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if visited[cur]:
                    continue
                visited[cur] = True
                for nextVertex in graph[cur]:
                    if visited[nextVertex]:
                        continue
                    if nextVertex==destination:
                        return True
                    q.append(nextVertex)
        return False