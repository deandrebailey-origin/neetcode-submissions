class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, 0
        best = 0

        c = []
        while r < k:
            heapq.heappush(c, (-nums[r], r))
            r+=1

        r -= 1    
        

        for i in range(len(nums) - k + 1):

            while c[0][1] < l:
                heapq.heappop(c)
            
            res.append(-c[0][0])

            r += 1
            l += 1

            if r < len(nums):
                heapq.heappush(c, (-nums[r], r))


        return res

        

