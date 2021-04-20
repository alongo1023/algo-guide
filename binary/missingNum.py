def missingNum(nums):
    '''
    :param nums: a list of numbers in range (0, len(nums)) except for one number
    :return: the number missing
    '''
    missing = 0
    for num in range(0, len(nums)+1):
        missing ^= num

    for num in nums:
        missing ^= num

    return missing

def main():
    assert(missingNum([0, 1, 3, 4, 5, 6, 7]) == 2)
    assert(missingNum([9, 3, 2, 5, 6, 8, 1, 0, 4]) == 7)
    assert(missingNum([5, 3, 2, 0, 1]) == 4)

main()

