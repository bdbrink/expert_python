class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        zero_count = 0
        
        # Right pointer moves through the array
        for right in range(len(nums)):
            # If we encounter a 0, increase the zero count
            if nums[right] == 0:
                zero_count += 1
            
            # If zero count exceeds k, shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # Move the left pointer to reduce the window size
            
            # Calculate the maximum length of the window
            max_length = max(max_length, right - left + 1)
        
        return max_length