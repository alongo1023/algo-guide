'''Given a list of numbers, nums, find the max area of a container given that coordinates are assumed to be
(index, nums[index]). No slanted lines allowed.'''
def maxArea(height):
    """
    :type height: List[int]
    :return: int
    """
    left = 0
    right = len(height) - 1
    maxArea = 0
    while left < right:
        leftH = height[left]
        rightH =height[right]
        width = right - left
        minHeight = min(leftH, rightH)
        currArea = width*minHeight
        maxArea = max(maxArea, currArea)
        #if left height is greater than right Height then hold left pointer and move right pointer
        #A bigger area will be potentially found by moving the right pointer
        if(leftH > rightH):
            right = right - 1
        else:
            #otherwise right height is bigger than left and a larger area could be found by moving the left pointer
            left = left + 1
    return maxArea

def main():
    heights1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert(maxArea(heights1)==49)

    heights2 = [4, 8, 10, 6, 20]
    assert (maxArea(heights2) == 24)

    heights3 = [3, 6, 1, 2, 5, 4]
    assert (maxArea(heights3) == 16)

    heights4 = [2, 3, 4, 1, 1, 1, 1, 1]
    assert (maxArea(heights4) == 7)




main()
