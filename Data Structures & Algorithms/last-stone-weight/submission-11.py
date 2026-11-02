class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        A = stones

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        print(A)

        while len(stones) >= 2:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            new = x - y
            if new != 0:
                heapq.heappush(stones,new)
            heapq.heapify(stones)
            
        
        if len(stones) == 1:
            return -stones[0]
        return 0 

        