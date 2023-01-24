class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        numberToIndex = [[] for _ in range(n**2+1)]
        i, j = n-1, 0
        right = True
        for index in range(1, n**2+1):
            numberToIndex[index] = [i, j]
            if right:
                j+=1
                if j==n:
                    i-=1
                    j-=1
                    right = False
            else:
                j-=1
                if j==-1:
                    j+=1
                    i-=1
                    right = True
        queue = deque([1])
        visited = [False for _ in range(n**2+1)]
        ans = -1
        while queue:
            size = len(queue)
            ans+=1
            for _ in range(size):
                cur = queue.popleft()
                if cur==n**2:
                    return ans
                if visited[cur]:
                    continue
                visited[cur] = True
                for nextValue in range(cur+1, min(cur+6, n**2)+1):
                    [i, j] = numberToIndex[nextValue]
                    if board[i][j]!=-1:
                        queue.append(board[i][j])
                        continue
                    if not visited[nextValue]:
                        queue.append(nextValue)
        return -1