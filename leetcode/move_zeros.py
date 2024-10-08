class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        # First, count and remove all the zeros
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zero += 1
            else:
                i += 1
        
        # Add the zeros back at the end
        nums.extend([0] * zero)