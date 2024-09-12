class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Count the frequency of each element using a hashmap
        freq_map = Counter(arr)  # Counter creates a dictionary with counts of each element
        
        # Step 2: Check if all frequencies are unique by using a set
        freq_set = set(freq_map.values())  # Convert the frequency values to a set
        
        # Step 3: If the size of the set is the same as the size of the frequency map, then all frequencies are unique
        return len(freq_map) == len(freq_set)