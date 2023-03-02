class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for s, e in redEdges:
            red[s].append(e)
        for s, e in blueEdges:
            blue[s].append(e)
        ans = [999 for _ in range(n)]
        q = deque([[0, 'b'], [0, 'r']])
        step = 0
        visited = defaultdict(list)
        visited['r'] = [False for _ in range(n)]
        visited['b'] = [False for _ in range(n)]
        while q:
            size = len(q)
            for _ in range(size):
                [current, color] = q.popleft()
                if visited[color][current]:
                    continue
                visited[color][current] = True
                ans[current] = min(ans[current], step)
                if color=='b':
                    for nextNode in red[current]:
                        q.append([nextNode, 'r'])
                else:
                    for nextNode in blue[current]:
                        q.append([nextNode, 'b'])
            step+=1
        for i in range(len(ans)):
            if ans[i]==999:
                ans[i] = -1
        return ans