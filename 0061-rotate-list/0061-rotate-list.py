# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # getting the length of the linked list
        length, tail = 1, head # length = 1 cause we know there there is one node--> the head for sure
        while tail.next:
            tail = tail.next
            length += 1

        # chekcing number of times to rotate
        k = k % length # to deal when k is greater than the length
        if k == 0:
            return head

        # chekcing where to rotate and rotating
        cur = head
        for i in range(length - k - 1): # here we do -1 because we are alread in the first head node. From this node to jump to the kth node (pivot) -> length - k - 1
            cur = cur.next

        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead


        