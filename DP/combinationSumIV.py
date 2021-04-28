'''Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.'''

def combinationSum4(nums, target):
    '''
    :param nums: List[int]
    :param target: int
    :return:
    '''
    dp = [0]*(target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for n in nums:
            if(i >= n):
                dp[i] = dp[i] + dp[i-n]

    return dp[target]

def main():
    assert(combinationSum4([1, 2, 3], 4) == 7)
    assert(combinationSum4([1,3], 2) == 1)
    assert(combinationSum4([5, 4, 1, 3], 9) == 53)

main()
