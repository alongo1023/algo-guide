def findMin(nums):
    'Given a rotated sorted array, find the min using binary search'
    left = 0
    right = len(nums) - 1

    if(nums[left] < nums[right]):
        #already sorted, return first element
        return nums[left]

    while left <= right:
        mid = left + int((right-left)/2)
        if(len(nums) == 1) :
            return nums[0]

        #if mid < mid -1, mid must be the min, mid and mid-1 are not sorted properly
        if(nums[mid] < nums[mid-1]):
            return nums[mid]
        if(nums[mid+1] < nums[mid]):
            #mid and mid+1 not ordered right, mid+1 must be min
            return nums[mid+1]

        if(nums[0] < nums[mid]):
            #check right side of array left side correctly sorted
            left = mid + 1
        else:
            right = mid - 1

def main():
    nums1 = [0, 1, 2, 3, 4]
    assert(findMin(nums1) == 0)

    nums2 = [7, 8, 10, 1, 3, 4]
    assert(findMin(nums2) == 1)

    nums3 = [9, 10, 11, 12, -3]
    assert(findMin(nums3) == -3)

    nums4 = [3]
    assert(findMin(nums4) == 3)

    nums5 = [5, 2]
    assert(findMin(nums5) == 2)
main()