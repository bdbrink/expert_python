class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            if char == "*":
                if stack:  # Only pop if the stack is not empty
                    stack.pop()
            else:
                stack.append(char)
        
        # Join the stack to form the final string
        return ''.join(stack)