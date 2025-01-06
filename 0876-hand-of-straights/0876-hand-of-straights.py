class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        handValues = list(count.keys()) # creating a list for the min heap using only the keys (distinct hand values)
        heapq.heapify(handValues)

        while handValues:
            first = handValues[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False

                count[i] -= 1
                if count[i] == 0: # we will have to pop this from the minHeap
                    if i != handValues[0]: # if the value we need to pop is not the first value in the min heap then we cannot pop it, and also even if we remove, we would not be bale to form othe next group because w eknoe that there is a value that is smaller than the i value we removed
                        return False
                    heapq.heappop(handValues)

        return True

