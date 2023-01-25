class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            if edges[i]!=-1:
                graph[i].append(edges[i])
        distance1 = self.bfs(graph, node1, len(edges))
        distance2 = self.bfs(graph, node2, len(edges))
        minValue = 10**5
        node = -1
        for index in range(len(edges)):
            if distance1[index]!=-1 and distance2[index]!=-1:
                localMax = max(distance1[index], distance2[index])
                if localMax<minValue:
                    minValue = localMax
                    node = index
        return node
    def bfs(self, graph, node, n):
        q = deque([node])
        distance = [-1 for _ in range(n)]
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                ele = q.popleft()
                if distance[ele]!=-1:
                    continue
                distance[ele] = step
                for nextNode in graph[ele]:
                    if distance[nextNode]==-1:
                        q.append(nextNode)
            step+=1
        return distance