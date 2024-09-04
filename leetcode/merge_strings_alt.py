
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_word = ""
        i = 0
        max_length = max(len(word1), len(word2))
        
        while i < max_length:
            if i < len(word1):
                final += word1[i]
            if i < len(word2):
                final += word2[i]
            i += 1
        
        return final_word