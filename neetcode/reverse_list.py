from typing import List

def reverse_list(arr: List[int]) -> List[int]:
    rvs_list = []
    while len(arr) > 0:
        num_reverse = arr.pop()
        rvs_list.append(num_reverse)
    
    return rvs_list

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
