# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        h = defaultdict(int)
        ans = []
        self.dfs(root,h,ans)
        
        return ans
    def dfs(self, root, h, ans):
        if not root:
            return "null"
        
        l = self.dfs(root.left, h, ans)
        r = self.dfs(root.right, h, ans)
        cur = str(root.val)+"l->"+l+"r->"+r
        h[cur]+=1
        if h[cur]==2:
            ans.append(root)
        return cur