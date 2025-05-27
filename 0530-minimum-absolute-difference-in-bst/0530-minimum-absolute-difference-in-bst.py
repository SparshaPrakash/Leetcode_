# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = float('-inf')
        min_diff = float('inf')

        def inorderTraversal(root):
            nonlocal prev, min_diff
            if not root:
                return

            # visiting the left subtree
            if root.left:
                inorderTraversal(root.left)

            # comparing the current node's value with the previous value
            if (root.val - prev) < min_diff:
                min_diff = root.val - prev

            # updating the previous value to the current node's value
            prev = root.val

            # in order traversal of the right sub tree
            if root.right:
                inorderTraversal(root.right)

        inorderTraversal(root)

        return min_diff

        