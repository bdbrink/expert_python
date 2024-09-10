class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize the sum of the first k elements
        current_sum = sum(nums[:k])
        
        # Initialize max_sum with the sum of first k elements
        max_sum = current_sum
        
        # Slide the window and update max_sum
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum average
        return max_sum / k