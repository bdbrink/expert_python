from typing import List

def remove_element(arr: List[int], element: int) -> List[int]:
    ### better solution
    # arr_clone = arr.copy()
    # arr_clone.remove(element)
    # return arr_clone
    
    new_list = list(arr)
    for x,y in enumerate(arr):
        if y == element:
            new_list.remove(element)

    return new_list


# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)