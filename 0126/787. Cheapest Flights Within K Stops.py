class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for s,e,p in flights:
            graph[s][e] = p
        cost = [2147483647 for _ in range(n)]
        cost[src] = 0
        q = deque([[src, 0]])
        for _ in range(k+1):
            size = len(q)
            for _ in range(size):
                [ele, curCost] = q.popleft()
                for nextNode in graph[ele]:
                    price = graph[ele][nextNode]
                    if price+curCost<cost[nextNode]:
                        cost[nextNode] = price+curCost
                        q.append([nextNode, price+curCost])
        if cost[dst]==2147483647:
            return -1
        return cost[dst]
