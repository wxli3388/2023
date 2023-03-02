class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        def dfs(node, parent):                       
            people = 1
            for child in adj[node]:
                if child != parent:
                    people += dfs(child, node)
            
            if node:
                self.result += (people - 1) // seats + 1
                
            return people
        
        adj = defaultdict(list)
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)
        
        self.result = 0
        dfs(0, None)
        
        return self.result