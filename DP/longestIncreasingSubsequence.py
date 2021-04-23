def lengthLIS(nums):
    '''
    :param nums: List[int]
    :return: int, length of longest increasing subsequence (does not need to be contiguous
    '''
    n = len(nums)
    memo = [1]*n
    maxResult = 1
    for j in range(1, n):
        for i in range(0, j):
            if(nums[j] < nums[i]):
                #not increasing, skip
                continue
            memo[j] = max(memo[i]+1, memo[j])
        maxResult = max(maxResult, memo[j])

    return maxResult

def main():
    assert(lengthLIS([-1, 3, 4, 5, 2, 2, 2, 2]) == 5)
    assert(lengthLIS([10,9,2,5,3,7,101,18]) == 4)
    assert(lengthLIS([0]) == 1)


main()