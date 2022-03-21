# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        level = [root]
        while root and level:
            cur_node = []
            nxtlvl = []
            for node in level:
                cur_node.append(node.val)
                if node.left:
                    nxtlvl.append(node.left)
                if node.right:
                    nxtlvl.append(node.right)
            ans.append(cur_node)
            level = nxtlvl
        return ans
        