def maxSubSequence(nums):
    #Find the max consecutive subsequence sum of a given array
    currentSum = nums[0]
    maxSum = nums[0]
    for num in nums[1:]:
        currentSum = max(num, currentSum+num)
        maxSum = max(currentSum, maxSum)

    return maxSum

def main():
    nums1 = [-1, 2, 5, 9, -2, 4]
    assert(18 == maxSubSequence(nums1))

    nums2 = [0]
    assert(0 == maxSubSequence(nums2))

    nums3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert(6 == maxSubSequence(nums3))

main()