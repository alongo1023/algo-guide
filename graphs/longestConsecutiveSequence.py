'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
'''

def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    numsSet = set(nums)
    maxLength = 0

    for num in nums:
        if num - 1 not in numsSet: #this num might be the start of the longest sequence
            currLength = 0
            while (num + currLength) in numsSet:
                currLength += 1
            maxLength = max(maxLength, currLength)
    return maxLength

def main():
    assert(longestConsecutive([1, 400, 2, 200, 3, 4]) == 4)
    assert(longestConsecutive([]) == 0)
    assert(longestConsecutive([0]) == 1)
    assert(longestConsecutive([99, 100, 300, 1000, 101, 1001, 102, 301, 1002, 103, 104, 105]) == 7)

main()
