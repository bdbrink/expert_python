class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # Using a set for faster lookups
        s = list(s)  # Convert string to a list to allow swapping
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move the left pointer to the next vowel
            if s[left] not in vowels:
                left += 1
            # Move the right pointer to the previous vowel
            elif s[right] not in vowels:
                right -= 1
            else:
                # Swap the vowels
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return ''.join(s)