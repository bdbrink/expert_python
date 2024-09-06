class Solution:
    def compress(self, chars: List[str]) -> int:
        
        write = 0  # This pointer will write the compressed characters
        i = 0      # This pointer will traverse the characters

        while i < len(chars):
            char = chars[i]
            count = 0

            # Count occurrences of the current character
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1

            # Write the character to the position `write`
            chars[write] = char
            write += 1

            # If the count is greater than 1, write the count as well
            if count > 1:
                for c in str(count):  # Handle counts with more than one digit
                    chars[write] = c
                    write += 1

        # The length of the new compressed list is `write`
        return write