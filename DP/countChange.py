def coinChange(coins, amount):
    '''
    :param coins: List[int] coins available to use
    :param amount: int amount needed to make change
    :return: minimum number of coins needed to make change
    '''
    # init DP list to be a large number
    placeholder = amount + 1
    # This list will contain the subproblem for each amount = index
    size = amount + 1
    minChange = [placeholder] * size
    minChange[0] = 0
    for i in range(1, size):
        for coin in coins:
            if (i < coin):
                # can not make change with the amount, i, and coin
                continue
            minChange[i] = min(minChange[i - coin] + 1, minChange[i])
    # if minChange[amount] is still placeholder, no solution was found given the parameters
    if (minChange[amount] == placeholder):
        return -1
    return minChange[amount]


def main():
    assert (coinChange([1, 2, 5], 11) == 3)
    assert (coinChange([1, 2, 5, 10], 45) == 5)
    assert (coinChange([5, 10], 8) == -1)

main()
