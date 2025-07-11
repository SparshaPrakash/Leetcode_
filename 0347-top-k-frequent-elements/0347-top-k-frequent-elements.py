class Solution(object):
    def topKFrequent(self, nums, k):
        d = defaultdict(int)
        for num in nums:
            d[num] += 1  # d = {1:3, 2:2,3:1, 4:3}
        heap = []  
        for key, val in d.items():
            if len(heap) < k or val > heap[0][0]:  # if the value is greater than the mimimum value in the heap
                heapq.heappush(heap,[val,key]) # val first here, vause it is sorted based on the firts value
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap] # retrning the values in the heap