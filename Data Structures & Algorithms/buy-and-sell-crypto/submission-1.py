class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        minPrice = prices[0]
        stack = []
        for i in range(len(prices)-1):
            #while stack and stack[-1] < prices[i]
            if minPrice > prices[i + 1]:
                minPrice = prices[i + 1]
            
            maxPrice = max(maxPrice, prices[i+1]-minPrice)
        return maxPrice

            
            

