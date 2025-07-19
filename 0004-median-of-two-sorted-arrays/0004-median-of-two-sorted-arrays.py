class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # number of elements in the left half
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2     # partition in nums1
            j = total_left - i          # partition in nums2

            # Handle edges: use -inf or +inf when out of bounds
            nums1_left_max  = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max  = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            # Check if we found a valid partition
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Correct partition found
                if (m + n) % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            elif nums1_left_max > nums2_right_min:
                # Too far right in nums1, move left
                right = i - 1
            else:
                # Too far left in nums1, move right
                left = i + 1
