'''Solve the 3Sums Problem, find all distinct triplets in a list that sum to 0'''

def threeSum(nums):
    triplets = []
    if len(nums) < 3:
        return triplets
    nums.sort()
    for i in range(0, len(nums)-2):
        #to avoid dups - since the list is sorted, if a neighbor element is the same we can ignore, already retrieved elements
        if i > 0 and nums[i]==nums[i-1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            currSum = nums[i] + nums[left] + nums[right]
            if currSum == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                #to avoid dups - move left pointer forward and right pointer back until no dups
                while left < right and nums[left] == nums[left+1]:
                    left = left + 1
                while left < right and nums[right] == nums[right-1]:
                    right = right - 1

                left = left + 1
                right = right - 1

            elif currSum < 0 :
                #we know that the only way to get closer to zero is by adding larger nums, so we move left forward
                left = left + 1

            elif currSum > 0:
                # we know that the only way to get closer to zero is by adding smaller nums, so we move right back
                right = right - 1

    return triplets


def main():
    nums1 = [-1,0,1,2,-1,-4]
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    assert(threeSum(nums1) == expected1)

    nums2 = [0, 0, 0, 0]
    expected2 = [[0, 0, 0]]
    assert(threeSum(nums2) == expected2)

    nums3 = [3, 5, 0, -8, 1, 2, -2, -3, -1, 3, 4, 0, 0, 2]
    expected3 = [[-8, 3, 5], [-3, -2, 5], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1], [0, 0, 0]]
    assert(threeSum(nums3) == expected3)

    nums4 = [1, 2, 3, 4]
    expected4 = []
    assert(threeSum(nums4) == expected4)


main()