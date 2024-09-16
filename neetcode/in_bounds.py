from typing import List

def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    rows, cols = len(grid), len(grid[0])

    if 0 <= r < rows and 0 <= c < cols:
        return True
    
    return False