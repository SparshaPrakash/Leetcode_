class Solution:
    def candy(self, ratings: List[int]) -> int:
        # rating [5 4 3  5 6 2]
        # we first iterate from left to right-> check if the left nae of current rating is lower, then add one candy to the current value
        # we then iterrate from right to left -> check if the righ nei of current val is lower, then add ome val to the current value only if the candy value is not already greater than its right nei
        arr = [1] * len(ratings)
        
        for i in range(1, len(ratings)): # element at index 0 doe snot have a left nei
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1
        
        for i in range(len(ratings) -2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                arr[i] = max(arr[i], arr[i + 1] + 1)

        return sum(arr)
        