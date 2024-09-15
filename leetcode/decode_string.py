class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []  # stack to hold numbers
        str_stack = []  # stack to hold intermediate strings
        current_str = ""  # string being built currently
        current_num = 0   # number being built currently
        
        for char in s:
            if char.isdigit():
                # Build the full number (handle cases like "10[a]")
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current number and string to the stacks
                num_stack.append(current_num)
                str_stack.append(current_str)
                # Reset for the new context inside the brackets
                current_num = 0
                current_str = ""
            elif char == ']':
                # Pop the number and previous string
                repeat_times = num_stack.pop()
                previous_str = str_stack.pop()
                # Build the string by repeating the current one
                current_str = previous_str + current_str * repeat_times
            else:
                # Build the current string
                current_str += char
        
        return current_str
