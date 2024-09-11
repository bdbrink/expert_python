class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            # If the right pointer encounters a 0, increase the zero count
            if nums[right] == 0:
                zero_count += 1
            
            # If there are more than one zero, move the left pointer to reduce the zero count
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # Shrink the window
            
            # Calculate the max length, -1 accounts for the one zero that needs to be removed
            max_len = max(max_len, right - left)
        
        return max_len