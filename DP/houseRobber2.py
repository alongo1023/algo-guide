'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place
are arranged in a circle. That means the first house is the neighbor of the
last one. Meanwhile, adjacent houses have a security system connected, and
it will automatically contact the police if two adjacent houses were broken
into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
'''
from DP.houseRobber import HouseRobber


def houseRobber2(nums: object) -> object:
    '''
    :param nums: List[int] -> value at each house
    :return: int -> max money you can steal
    '''
    if len(nums) == 1:
        return nums[0]
    return max(nums[0], HouseRobber.rob(nums[1:]), HouseRobber.rob(nums[:-1]))


def main():
    assert (houseRobber2([0, 0]) == 0)
    assert (houseRobber2([2]) == 2)
    assert (houseRobber2([1, 2, 1, 1]) == 3)
    assert (houseRobber2([2, 1, 1, 2]) == 3)
    assert (houseRobber2([1, 1, 1, 2]) == 3)


main()
