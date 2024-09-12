class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Use sets to remove duplicates and optimize the difference calculation
        set1 = set(nums1)
        set2 = set(nums2)

        # Find elements in set1 that are not in set2, and vice versa
        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)

        return [diff1, diff2]