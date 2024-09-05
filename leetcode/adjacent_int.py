class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        plantable = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == length - 1 or flowerbed[i + 1] == 0)

                if prev_empty and next_empty:
                    # We can plant a flower here
                    flowerbed[i] = 1
                    plantable += 1
                
                if plantable >= n:
                    return True

        return plantable >= n