'''
Buy and Sell Stocks
profit = selling price - buying price

buying variable to store lowest buying stock 

'''
import sys

def buyANdsell(prices):
    buyingPrice = +sys.maxsize
    maxProfit = 0

    for i in range(len(prices)):
        if buyingPrice < prices[i]:
            profit = prices[i] - buyingPrice # today profit
            if maxProfit < profit:
                maxProfit = profit
        else:
            buyingPrice = prices[i]
    
    return maxProfit
        


price = [7,1,5,3,6,4]

print(buyANdsell(price))