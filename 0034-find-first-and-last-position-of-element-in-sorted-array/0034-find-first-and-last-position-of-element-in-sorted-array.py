class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)

        return [left, right]


    # leftBias = True or False, if false, res is rightBiased
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m # shifting the index to the midle value
                if leftBias: # if we are looking for the left index
                    r = m - 1
                else:  # if we are looking for thr right index
                    l = m + 1
        return i        