class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
    # Step 1: Merge the two sorted arrays
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Add any remaining elements
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        # Step 2: Find the median
        n = len(merged)
        if n % 2 == 1:
            # Odd length -> middle element
            return float(merged[n // 2])
        else:
            # Even length -> average of two middle elements
            mid1 = merged[n // 2 - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2.0

            