class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp, max_profit = prices[0], 0
        for day, sp in enumerate(prices):
            if day == 0:
                continue
            bp = min(bp, prices[day-1])
            max_profit = max(max_profit, sp - bp)
        return max_profit
        
            