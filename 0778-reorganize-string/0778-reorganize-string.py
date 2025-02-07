class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) # __> count, char
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            # getting the most freq char except the previously used value
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1 # count = count - 1, but since we are using negaitive values initaiily for maxHeap, we use + here

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res
        