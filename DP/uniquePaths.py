'''Given a m x n grid, and a start of (1, 1) find the number of ways to get to
(m, n) if only allowed to go down or to the right'''

def uniquePaths(m, n):
    '''
    :param m: int
    :param n: int
    :return: int
    '''
    dp =[[0 for y in range(n+1)] for x in range(m+1)]
    dp[1][1] = 1
    for x in range(1, m+1):
        for y in range(1, n+1):
            dp[x][y] = dp[x][y] + dp[x-1][y] + dp[x][y-1]

    return dp[m][n]

def main():
    assert(uniquePaths(3, 2) == 3)
    assert(uniquePaths(3, 3) == 6)
    assert(uniquePaths(3, 7) == 28)

main()