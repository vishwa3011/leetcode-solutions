class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ## maximum profit is buying at a very less price and selling on a very high price
        
        j = 1
        buy_price = float('inf')
        max_profit = 0
        
        for i in range(len(prices)-1):
            
            if prices[i] < buy_price:
                buy_price = prices[i]
                
            sell_price = prices[j]
            profit = sell_price - buy_price
            
            if profit > max_profit:
                max_profit = profit
            
            j += 1
            
        return max_profit