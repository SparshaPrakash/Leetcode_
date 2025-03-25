class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        cur_pos = 1
        last_freq = 1
        last_ele = nums[0]

        while cur_pos < len(nums):
            if nums[cur_pos] == last_ele:
                if last_freq < 2:
                    nums[i] = nums[cur_pos]
                    i += 1
                    last_freq += 1
            else:
                nums[i] = nums[cur_pos]
                i += 1
                last_freq = 1
                last_ele = nums[cur_pos]
            cur_pos += 1

        return i
