class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # Update cheapest buying price seen so far
            min_price = min(min_price, price)

            # Profit if we bought at min_price and sold today
            profit = price - min_price

            # Keep the best profit we've seen
            max_profit = max(max_profit, profit)

        return max_profit