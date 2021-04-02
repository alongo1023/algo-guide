def maxProduct(nums):
    '''Given a list of nums find the maximum product of a a consecutive subarray
    Assume nums can be negative or positive'''
    maxResult = max(nums)
    currMin = 1
    currMax = 1
    for num in nums:
        if(num == 0):
            currMin = 1
            currMax = 1
            continue
        tempMax = currMax
        currMax = max(num, num*tempMax, num*currMin)
        currMin = min(num, num*currMin, num*tempMax)
        maxResult = max(maxResult, currMax)
    return maxResult

def main():
    nums1 = [-2, 3, 4, -1]
    assert(maxProduct(nums1) == 24)

    nums2 = [0, 1, -1, 0]
    assert(maxProduct(nums2) == 1)

    nums3 = [-2, 0]
    assert(maxProduct(nums3) == 0)

main()
