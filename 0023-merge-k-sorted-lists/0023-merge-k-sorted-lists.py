import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For printing/debugging
    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Step 1: Push the head of each list into the heap
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        dummy = ListNode()
        tail = dummy

        # Step 2: Keep popping the smallest element and push its next
        while heap:
            val, idx, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next