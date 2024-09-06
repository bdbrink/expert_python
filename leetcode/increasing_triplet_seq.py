class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize two variables to hold the smallest and second smallest values.
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # Update first if current number is smaller.
            elif num <= second:
                second = num  # Update second if current number is between first and second.
            else:
                # If we find a number greater than both first and second, return True.
                return True
        
        # If no such triplet is found, return False.
        return False