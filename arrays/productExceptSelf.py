def productExceptSelf(nums):
   '''
   Given an integer array nums, return an array answer such that answer[i] is equal
   to the product of all the elements of nums except nums[i]
   '''
   n = len(nums)
   'create left and right array to keep track of left and right products at each index'
   left = [0] * n
   right = [0] * n
   left[0] = 1
   right[n - 1] = 1
   product = [0] * n
   for i in range(1, n):
       left[i] = left[i - 1] * nums[i - 1]
       right[n - 1 - i] = right[n - i] * nums[n - i]
   for i in range(0, n):
       product[i] = left[i] * right[i]
   return product

def main():
    nums = [1, 2, 3, 4]
    assert(productExceptSelf(nums)==[24, 12, 8, 6])

    nums2 = [-1,1,0,-3,3]
    assert(productExceptSelf(nums2) == [0, 0, 9, 0, 0])
main()