def twoSum(nums, target):
    #nums is a list of integers
    #target is the target sum of two ints from nums
    complementMap = {}
    for i in range(0, len(nums)):
        x = nums[i]
        y = target - x
        if y in complementMap and complementMap[y]!=i:
            #returns two indices that give you the values that sum to target
            return i, complementMap[y]
        complementMap[x] = i
    print("No two sum in list")

def main():
    nums1 = [1, 2, 3, 4]
    target1 = 6
    result1 = twoSum(nums1, target1)
    assert(1 in result1 and 3 in result1)

    nums2 = [3, 3]
    target2 = 6
    result2 = twoSum(nums2, target2)
    assert (1 in result2 and 0 in result2)

    nums3 = [-2, -3, 1, -6]
    target3 = -8
    result3 = twoSum(nums3, target3)
    assert(0 in result3 and 3 in result3)


main()