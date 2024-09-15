from typing import List, Deque
from collections import deque

def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque(arr)
    for i in range(k):
        num = queue.pop()
        queue.appendleft(num)
    return queue

# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))