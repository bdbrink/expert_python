class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: Check if the sets of unique characters are the same
        if set(word1) != set(word2):
            return False
        
        # Step 2: Count the frequency of each character in both words
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        # Step 3: Compare the sorted frequency values
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True