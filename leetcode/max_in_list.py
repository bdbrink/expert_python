class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kiddos = []
        greatest_candy = max(candies)
        for candy in candies:
            new_total = candy + extraCandies
            if new_total >= greatest_candy:
                kiddos.append(True)
            else:
                kiddos.append(False)
        
        return kiddos