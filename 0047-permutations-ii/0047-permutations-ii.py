class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {n:0 for n in nums} # creating a hashmap to store the count of ecah number

        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())

                return

            for n in count:
                if count[n] > 0:  # checking if we still have enough of the current values
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1  # adding back the value to get the next set of permutaion
                    perm.pop()

        dfs()
        return res


        