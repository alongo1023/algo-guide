def containsDups(nums):
    #hashtable of values that have already been seen
    checkedSet = set()
    for num in nums:
        if num in checkedSet:
            return True
        else:
            checkedSet.add(num)

    return False

def main():
    nums1 = [1,4, 7, 1, 2, 4]
    assert(containsDups(nums1))

    nums2 = [1, 4, 7, 6]
    assert (not containsDups(nums2))

    nums3 = [0, -2, -2, 10]
    assert (containsDups(nums3))


main()