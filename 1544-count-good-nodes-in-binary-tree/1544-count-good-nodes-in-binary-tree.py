# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(root, maxVal):
            if root.val >= maxVal:
                self.good += 1
            if root.left:
                dfs(root.left, max(maxVal, root.val))
            if root.right:
                dfs(root.right, max(maxVal, root.val))

        dfs(root, root.val)
        return self.good
        