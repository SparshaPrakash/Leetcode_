class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        res = {}
        i = 0
        minHeap = []

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r)) # to the min heap, we are adding the length of the interval and also the right value, so if the lengths of 2 intervals are the same, we could use the one which has a lesser right/end value
                i += 1

            # popping the irrelvant values from the min heap
            while minHeap and minHeap[0][1] < q: # if the end/right value in the first value of the minheap is lesser than the q value, then that interval ends much before the q value, so we do not need such intervals
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1 # getting the smallest value from the min heap and getting the lenth og the interval from the firts value

        return [res[q] for q in queries] # the res is origibally a hashmap, so here we are converting it to a list which is in the same order as the queries in the question

# Time complexity- O(n log n + q log q) n is the length of intervals, q is the length of queries 
        