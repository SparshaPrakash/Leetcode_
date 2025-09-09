# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q_nodes = deque([(p, q)])   # queue holds pairs of nodes

        while q_nodes:
            node1, node2 = q_nodes.popleft()

            if not node1 and not node2:
                continue   # both None → fine, skip
            if not node1 or not node2:
                return False   # one None → mismatch
            if node1.val != node2.val:
                return False   # values differ → mismatch

            # enqueue children as pairs
            q_nodes.append((node1.left, node2.left))
            q_nodes.append((node1.right, node2.right))

        return True
        