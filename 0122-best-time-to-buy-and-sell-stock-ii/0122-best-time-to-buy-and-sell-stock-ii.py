class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_price = float('inf')
        max_profit = 0
        j = 1
        n = len(prices)
        
        for i in range(n):
            
            if prices[i] < buy_price:
                buy_price = prices[i]
            
            sell_price = prices[i]
            profit = sell_price - buy_price
            
            
            if j < n:
                if prices[j] < prices[i]:
                    max_profit += profit
                    buy_price = prices[j]
                   
            j += 1
        
        max_profit += profit
        
        return max_profit