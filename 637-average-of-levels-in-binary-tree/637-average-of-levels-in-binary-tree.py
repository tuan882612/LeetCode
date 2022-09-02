# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = []
        queue.append(root)

        while queue:
            length = len(queue)
            temp = []

            while length > 0:
                node = queue.pop(0)
                temp.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                length-=1

            res.append(sum(temp)/len(temp))

        return res