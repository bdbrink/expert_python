class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)  # Total sum of the array
        
        for i in range(len(nums)):
            total -= nums[i]  # Remove the current element from the total sum (this gives us the right side sum)
            
            if left == total:  # If the left sum equals the right sum, return the index
                return i
            
            left += nums[i]  # Add the current element to the left sum
        
        return -1