# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/stock-buy-and-sell2615

class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        n = len(prices)
        local_minima = local_maxima = prices[0]
        profit = 0

        i = 0
        while i < n-1:

            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1

            local_minima = prices[i]

            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1

            local_maxima = prices[i]

            profit += (local_maxima-local_minima)

        return profit
    
    def maximumProfit2(self, prices) -> int:
        # code here
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit
    

if __name__ == '__main__':
    test = Solution()
    print(test.maximumProfit([100, 180, 260, 310, 40, 535, 695]))
    print(test.maximumProfit2([100, 180, 260, 310, 40, 535, 695]))