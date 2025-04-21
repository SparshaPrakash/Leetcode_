# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right
        # we will add the nodes lesser than x to the left list and the nodes greater than x to the right list
        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        ltail.next = right.next
        rtail.next = None
        return left.next

        






        # # get pos of x = x_pos
        # # traverse now if ele < x then check if pos is < x_pos
        # # if yes do nothing else, swap x_pos x and pos 
        # node = head
        # x_pos = 0
        # while node is not None:
        #     x_pos += 1
        #     if node.val == x:
        #         break
        #     node = node.next
        # node = head
        # ctr = 0
        # while node is not None:
        #     # greater ptr > than pos
        #     # lesser ptr < pos
        #     ctr += 1
        #     if node.val < x and ctr >= x_pos:
        #         # swap
        #     if node.val >= x and ctr < x_pos:
        #         # swap
        #     node = node.next

            
            

        