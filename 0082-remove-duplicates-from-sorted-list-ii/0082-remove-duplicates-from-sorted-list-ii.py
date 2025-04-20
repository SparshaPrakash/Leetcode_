# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur:
            # chekcing if its a dupliacte
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # now cur is the last duplicate value
                prev.next = cur.next
            else:
                # no duplactes present
                prev = prev.next # move prev value only if cur was not a duplivaye
            cur = cur.next # we need to move cur in all cases
            

        return dummy.next