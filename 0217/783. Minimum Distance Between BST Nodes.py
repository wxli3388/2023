# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        def traversal(root, arr):
            if not root:
                return
            traversal(root.left, arr)
            arr.append(root.val)
            traversal(root.right, arr)
        traversal(root, arr)
        ans = 999999
        for i in range(1, len(arr)):
            ans = min(ans, abs(arr[i]-arr[i-1]))
        return ans