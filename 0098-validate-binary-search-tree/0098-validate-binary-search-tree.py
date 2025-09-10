# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            node, lo, hi = stack.pop()
            if not (lo < node.val < hi):
                return False

            if node.right:
                stack.append((node.right, node.val, hi))
            if node.left:
                stack.append((node.left, lo, node.val))

        return True
