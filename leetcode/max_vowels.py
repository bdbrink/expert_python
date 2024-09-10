class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        
        # Count vowels in the first k characters
        count = sum(1 for char in s[:k] if char in vowels)
        
        # Initialize max_count with the count of first k characters
        max_count = count
        
        # Slide the window and update max_count
        for i in range(k, len(s)):
            # Remove the contribution of the character leaving the window
            if s[i-k] in vowels:
                count -= 1
            
            # Add the contribution of the character entering the window
            if s[i] in vowels:
                count += 1
            
            # Update max_count if necessary
            max_count = max(max_count, count)
        
        return max_count