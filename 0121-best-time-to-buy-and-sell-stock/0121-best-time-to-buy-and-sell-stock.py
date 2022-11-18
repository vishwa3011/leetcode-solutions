class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ## maximum profit is buying at a very less price and selling on a very high price
        
        buy_price = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            
            if prices[i] < buy_price:
                buy_price = prices[i]
                
            sell_price = prices[i]
            profit = sell_price - buy_price
            
            if profit > max_profit:
                max_profit = profit
            
            
        return max_profit