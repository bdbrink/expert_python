class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # Initialize the result array with 1s.
        
        # Step 1: Fill result with the product of all elements to the left of each index
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Step 2: Multiply with the product of all elements to the right of each index
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result