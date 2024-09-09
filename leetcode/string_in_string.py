class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        how_many = len(s)
        truth = 0
        for char in s:
            if char in t:
                truth += 1

        if truth == how_many:
            return True
        else:
            return False