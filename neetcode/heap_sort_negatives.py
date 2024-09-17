import heapq
from typing import List

def get_reverse_sorted(nums: List[int]) -> List[int]:
    rvs_list = []
    sorted_list = []
    for num in nums:
        heapq.heappush(rvs_list, -num)
    
    while rvs_list:
        positive_int = -heapq.heappop(rvs_list)
        sorted_list.append(positive_int)
    return sorted_list

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
