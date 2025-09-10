# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None          # last visited value in inorder

        cur = root
        while cur or stack:
            # go left
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            # inorder must be strictly increasing (no duplicates allowed)
            if prev is not None and cur.val <= prev:
                return False
            prev = cur.val

            # then go right
            cur = cur.right

        return True

