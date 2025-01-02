class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M , R):
            left_half = arr[L:M+1]
            right_half = arr[M + 1:R + 1]
            # merging the values
            i, k, j = L, 0, 0 # to fill in the array using index i

            while k < len(left_half) and j < len(right_half):
                if left_half[k] <= right_half[j]:
                    arr[i] = left_half[k]
                    k += 1
                else:
                    arr[i] = right_half[j]
                    j += 1
                i += 1

            while k < len(left_half):
                nums[i] = left_half[k]
                k += 1
                i += 1

            while  j < len(right_half):
                nums[i] = right_half[j]
                j += 1
                i += 1


        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)

            merge(arr, l, m, r)
            return arr

        mergeSort(nums, 0, len(nums) - 1)
        return nums
        