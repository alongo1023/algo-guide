'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
'''

def canJump(nums):
    '''
    :param nums: List[int]
    :return: bool
    '''
    end = len(nums) - 1
    for i in range(end-1, -1, -1):
        if(nums[i]+i >= end):
            end = i

    return end == 0

def main():
    assert(canJump([2, 3, 1, 1, 4]))
    assert(not canJump([3, 2, 1, 0, 4]))
    assert(not canJump([0, 1]))
    assert(canJump([1]))


main()