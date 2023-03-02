class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    q.append([i, j])
        if len(q)==len(grid)*len(grid[0]):
            return -1
        step = -1
        while q:
            size = len(q)
            for _ in range(size):
                [x, y] = q.popleft()
                for dx, dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                    nx, ny = dx+x, dy+y
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==0:
                        grid[nx][ny] = 1
                        q.append([nx, ny])
            step+=1
        return step