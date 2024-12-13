#approach is simple, what you do is just check always for the minimium, then, subtract for the price of the current iteration, then, see if the difference
#aka profit is bigger than the previous.
class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = 999999999
        
        for price in prices:
            minPrice = min(minPrice, price) # see what is the minimum
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        
        return maxProfit
