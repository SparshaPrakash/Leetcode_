# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def helper(self, prev, curr):
            if curr is None:
                return prev
            next_node = curr.next
            curr.next = prev
            next_head = self.helper(curr, next_node)
            return next_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(None, head)

        
        # curr = head
        # prev = None


        # while curr != None:
        #     next_node = curr.next
        #     curr.next = prev

        #     prev = curr
        #     curr = next_node

        # return prev

       







        
         
        