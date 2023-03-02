"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.solve(grid, 0, 0, n)
    def solve(self, grid, x, y, n):
        if n==1:
            return Node(grid[x][y], True)
        
        topLeft = self.solve(grid, x, y, n//2)
        topRight = self.solve(grid, x, y+n//2, n//2)
        bottomLeft = self.solve(grid, x+n//2, y, n//2)
        bottomRight = self.solve(grid, x+n//2, y+n//2, n//2)
        
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val==topRight.val and topRight.val==bottomLeft.val and bottomLeft.val==bottomRight.val:
            return Node(topLeft.val, True)
        return Node(-1, False, topLeft, topRight, bottomLeft, bottomRight)