class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_sellingpt = 0
        i, j = 0, 1
        max_profit = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                if profit > max_profit: max_profit = profit
            else:
                i=j
            j+=1
        return max_profit
