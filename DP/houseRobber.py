'''You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security systems
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return
the maximum amount of money you can rob tonight without alerting the police.
 '''

class HouseRobber(object):
    def rob(nums):
        '''
        :param nums: List[int] value at each house
        :return: int, max money you can rob
        '''
        n = len(nums)
        if (n == 1):
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]


def main():
    assert (HouseRobber.rob([1, 2, 3, 1]) == 4)
    assert (HouseRobber.rob([2, 7, 9, 3, 1]) == 12)
    assert (HouseRobber.rob([4, 5, 1, 10]) == 15)
    assert (HouseRobber.rob([2, 9, 5, 1, 3, 4, 3, 3, 3, 3]) == 20)


main()
