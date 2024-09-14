class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:
            # Check for collisions
            while stack and asteroid < 0 and stack[-1] > 0:
                # Compare the last asteroid in the stack with the current one
                if stack[-1] < -asteroid:  # stack asteroid is smaller and gets destroyed
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:  # both are of the same size and destroy each other
                    stack.pop()
                break
            else:
                # If no collision happens, push the asteroid to the stack
                stack.append(asteroid)