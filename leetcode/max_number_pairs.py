class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        count_map = defaultdict(int)  # To store frequencies of numbers
        operations = 0
        
        for num in nums:
            complement = k - num
            # If the complement exists in count_map, we can form a pair
            if count_map[complement] > 0:
                operations += 1
                count_map[complement] -= 1  # Use up one complement
            else:
                # Otherwise, store the current number in the map
                count_map[num] += 1
        
        return operations