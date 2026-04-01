class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0

        for p in prices: 
            if p < minPrice:
                minPrice = p
            else:
                maxProfit = max(maxProfit, p - minPrice)
        
        return maxProfit