class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # first we keep a count of each letter
        # we had the counts in maxHeap (by taking negatives of the actual count)
        # we increase the time variabke by 1 after every operation
        # after using one charcter (strating with char with the most freq), we pop that char from maxHeap for now 
        # we reduce that char count by 1 and add it in a queue, and also add the time in which we can add it back to the maxHeap, so that it can be used again after the given idle time (time + n)
        

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of the decreased char count after using it and the idle time for it]
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # reducing the count
                if cnt:  # if count is 0, we are done using that char so we do not have to do anything
                    q.append([cnt, time + n])
            if q and q[0][1] == time: # if the idle time foe that particular char has been reached
                heapq.heappush(maxHeap, q.popleft()[0]) # adding the char back in the maxHeap so that it can be used again
        return time

                
        