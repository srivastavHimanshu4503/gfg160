# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/buy-stock-2

class Solution:
    def maximumProfit(self, prices):
        # code here
        res = 0
        minima = prices[0]

        for i in range(1, len(prices)):
            minima = minima if minima < prices[i] else prices[i]

            res = res if res > (prices[i] - minima) else (prices[i] - minima)

        return res