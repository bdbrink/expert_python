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

class SolutionBetter:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointers for both strings
        s_pointer, t_pointer = 0, 0
        
        # Loop through t while checking for subsequence in s
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1
        
        # If we have matched all characters in s, return True
        return s_pointer == len(s)