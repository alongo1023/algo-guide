def knapsack(maxW, wts, vals):
    numItems = len(wts)
    dp = [[0 for i in range(maxW+1)] for j in range(numItems + 1)]
    for itemNum in range(1, numItems + 1):
        for capacity in range(1, maxW + 1):
            if(capacity < wts[itemNum - 1]):
                continue
            else:
                valWith = dp[itemNum-1][capacity - wts[itemNum - 1]] + vals[itemNum - 1]
                valWithout = dp[itemNum-1][capacity]
                dp[itemNum][capacity] = max(valWith, valWithout)
    return dp[numItems][maxW]

def main():
    wts = [5, 4, 6, 3]
    vals = [10, 40, 30, 50]
    maxW = 10
    assert(knapsack(maxW, wts, vals) == 90)

main()