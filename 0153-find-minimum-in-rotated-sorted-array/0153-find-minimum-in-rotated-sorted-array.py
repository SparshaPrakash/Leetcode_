class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) //2
            if nums[l] <= nums[m]:  # left side is sorted
                res = min(res, nums[l])
                l = m + 1
            else:
                res = min(res, nums[m]) 
                r = m - 1


        return res

        

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# get the middle term -> 7
# chekc if left is lesser than m
# move l to m + 1

# [4,5,6,7,0,1,2]
# l            #r
# middle, m = nums[m] = 7
#l = m + 1 = index 4
# [4,5,6,7,0,1,2]
          #l #r
          #m = 1


# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         res = nums[0]
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             if nums[l] < nums[r]:
#                 res = min(res, nums[l])
#                 break

#             m = l + ((r - l) // 2)
#             res = min(res, nums[m])
#             if nums[m] >= nums[l]:
#                 l = m + 1
#             else:
#                 r = m - 1

#         return res
        

#         # []
