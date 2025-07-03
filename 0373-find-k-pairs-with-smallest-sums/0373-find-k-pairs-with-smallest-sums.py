class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2 or k == 0:
            return []

        # Min-heap to store (sum, i, j)
        # Where i is index from nums1 and j is index from nums2
        heap = []
        res = []

        # Push first k pairs from the first row (nums1[i] + nums2[0])
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        # Extract the k smallest pairs
        while heap and len(res) < k:
            total, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            # If there's a next element in nums2, push (i, j+1)
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res