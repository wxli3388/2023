# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        arr = []
        while q:
            size = len(q)
            temp = []
            for _ in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                temp.append(cur.val)
            arr.append(temp)
        for i in range(len(arr)):
            if i%2==1:
                arr[i] = arr[i][::-1]
        return arr
                