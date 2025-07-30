# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        # Find left subtree size
        left_root = preorder[1]
        left_size = postorder.index(left_root) + 1
        
        root.left = self.constructFromPrePost(preorder[1:left_size+1], postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[left_size+1:], postorder[left_size:-1])
        
        return root
