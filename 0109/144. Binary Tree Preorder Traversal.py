# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.traversal(root, ans)
        return ans
    def traversal(self, root, arr):
        if not root:
            return
        arr.append(root.val)
        self.traversal(root.left, arr)
        self.traversal(root.right, arr)
