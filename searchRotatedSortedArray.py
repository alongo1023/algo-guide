'''
This program searches for a target element in an array that is sorted
but could have potentially been rotated. Using a binary search approach
the search time is O(logn)
'''
def searchDriver(nums, target):
    return search(nums, 0, len(nums)-1, target)

def search(nums, left, right, target):
    if(left>right):
        return -1

    mid = left + (right-left)//2
    if(nums[mid]==target):
        return mid

    #If left half of array is sorted
    if(nums[left] <= nums[mid]):
        #if target is in range of left half then search left half
        if(target>=nums[left] and target <= nums[mid]):
            return search(nums,left, mid-1, target)
        else:#otherwise search right
            return search(nums, mid+1, right, target)


    #If we make it here, the right side is sorted and we check which side target is
    if(target <= nums[right] and target>=nums[mid]):
        #target is on the right side
        return search(nums, mid+1, right, target)
    # otherwise target is on left side
    return search(nums, left, mid-1, target)





def main():
    nums1 = [3, 1]
    assert(searchDriver(nums1, 1) == 1)

    nums2 = [5, 1, 2, 3, 4]
    assert(searchDriver(nums2, 5) == 0)

    nums3 = [0, 1, 2, 4, 9]
    assert(searchDriver(nums3, 9) == 4)

    nums4 = [8]
    assert(searchDriver(nums4, 1) == -1)

main()