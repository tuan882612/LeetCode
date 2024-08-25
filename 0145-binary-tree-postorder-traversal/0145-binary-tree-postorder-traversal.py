# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.dfs(root, arr)
        return arr
        
    def dfs(self, root, key):
        if root:
            self.dfs(root.left, key)
            self.dfs(root.right, key)
            key.append(root.val)