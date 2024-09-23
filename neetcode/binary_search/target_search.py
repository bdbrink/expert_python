class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target not in nums:
            return -1
        
        for index,num in enumerate(nums):
            if num == target:
                return index