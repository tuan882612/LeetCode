# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        self.dfs(root, arr)
        cur = min(arr)
        res = max(arr)  
        
        for i in range(1,len(arr)):
            res = min(arr[i]-arr[i-1], res)
            
        return res

    def dfs(self, root, arr):
        if root:
            self.dfs(root.left, arr)
            arr.append(root.val)
            self.dfs(root.right, arr)