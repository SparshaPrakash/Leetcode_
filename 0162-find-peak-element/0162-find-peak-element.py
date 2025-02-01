class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # getting the middle lement, and chekcing if side of it has a value greater than the middle value, the peak would liw there, there woulc be a peak on the other side too, but htis side that we aee checking, it owuld be guaranteed to find a peak

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            # chwcking of the left side of m id greater than m
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1

            elif m < len(nums) -1 and nums[m] <nums[m + 1]:
                l = m + 1
            else:
                return m
        