class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        current_altitude = 0
        max_altitude = 0
        
        # Iterate through the gain list to calculate the altitude at each step
        for g in gain:
            current_altitude += g  # Add the current gain to the altitude
            max_altitude = max(max_altitude, current_altitude)  # Track the maximum altitude

        return max_altitude