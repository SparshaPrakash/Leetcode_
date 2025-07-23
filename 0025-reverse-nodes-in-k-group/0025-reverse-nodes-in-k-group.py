# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: add a dummy node before head
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            # Step 2: find kth node from groupPrev
            kth = self.getKth(groupPrev, k)
            if not kth:  # not enough nodes left
                break
            groupNext = kth.next  # node after the kth node

            # Step 3: reverse from groupPrev.next to kth
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Step 4: reconnect
            temp = groupPrev.next  # this becomes the tail after reverse
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Move k steps ahead from curr
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
