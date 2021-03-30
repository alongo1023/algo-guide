
def maxProfit(prices):
    #Given a list of stock prices, where index represents day, find the max profit if you were to buy and then sell that stock in order
    buy = 100000
    maxProfit = 0
    for price in prices:
        if (price - buy > maxProfit):
            maxProfit = price - buy
        if(price < buy):
            buy = price
    return maxProfit

def main():
    prices1 = [4, 6, 1, 5, 10]
    assert(maxProfit(prices1) == 9)

    prices2 = [5]
    assert(maxProfit(prices2) == 0)



main()