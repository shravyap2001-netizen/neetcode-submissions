class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0 
        for i, j in enumerate(prices):
            if j < prices[left]:
                left = i
            profit = j - prices[left]
            max_profit = max(max_profit,profit)
            
        return max_profit
