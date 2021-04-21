def climbStairs(n):
    '''
    :param n: Number of steps in a staircase
    :return: Given you can either take 1 step or 2 steps at a time,
    return the number of unique paths
    example: n=5 -> [{1, 1, 1, 1, 1}, {2, 2, 1}, {1, 2, 2}, {2, 1, 2},
                    {1, 2, 1, 1}, {1, 1, 2, 1}, {2, 1, 1, 1}, {1, 1, 1, 2}]
            return = 8
    '''
    if(n==0):
        return 0
    climb = [0]*(n+1)
    climb[1] = 1#1 way to climb one step
    climb[2] = 2#2 ways to climb two steps
    for i in range(3, n+1):
        #climb[i] is the number of steps to take 1 step from i-1 + 2 steps from i-2
        climb[i] = climb[i-1]+climb[i-2]

    return climb[n]


def climbRecursiveDriver(n):
    #A brute force way to do this is recursively
    if(n==0):
        return 0
    memo = [0]*(n+1)
    return climbRecursive(n, 0, memo);

def climbRecursive(n, i, memo):
    if(i>n):
        return 0
    if(i==n):
        return 1
    if(memo[i] > 0):
        return memo[i]
    memo[i] = climbRecursive(n, i+1, memo) + climbRecursive(n, i+2, memo)
    return memo[i]

def main():
    assert(climbRecursiveDriver(5) == 8)
    assert(climbStairs(5) == 8)

    assert(climbRecursiveDriver(0) == 0)
    assert (climbStairs(0) == 0)

    assert (climbRecursiveDriver(1) == 1)
    assert (climbStairs(2) == 2)

    assert (climbRecursiveDriver(2) == 2)
    assert (climbStairs(2) == 2)

    assert (climbStairs(10) == 89)

    assert(climbStairs(40) == 165580141)

main()