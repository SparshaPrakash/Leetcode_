class Solution(object):
    def twoSum(self, nums, target):
        valueIndex = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in valueIndex:
                return [valueIndex[diff],i]
            valueIndex[nums[i]] = i
        return

        