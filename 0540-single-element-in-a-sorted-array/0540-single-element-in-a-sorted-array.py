class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:  # No need for `<=` because the result will be in a single element
            m = l + (r - l) // 2

            # Check if `m` is the single element
            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and 
                (m + 1 == len(nums) or nums[m] != nums[m + 1])):
                return nums[m]

            # Determine if the left side has an odd number of elements
            if (m % 2 == 0 and nums[m] == nums[m + 1]) or (m % 2 == 1 and nums[m] == nums[m - 1]):
                l = m + 1
            else:
                r = m - 1

        return nums[l]  # `l` will point to the single element
