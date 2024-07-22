
def merge_update():
    list1 = [1,2,3]
    list2 = [4,5,6]
    
    merge_list = list1 + list2
    print(merge_list)
    
    value = (1,2,3)
    value += (4,5,6)
    print(value)

print("#### Merge Update ###")
merge_update()
print("#### Merge Update ###")

def binary_operators():
    # intersection &
    # union |
    # difference -
    # symmetric ^
    
    ex1 = {1,2,3} & {1,4}
    print(ex1)
    
    ex2 = {1,2,3} | {1,4}
    print(ex2)
    
    ex3 = {1,2,3} - {1,4}
    print(ex3)
    
    ex4 = {1,2,3} ^ {1,4}
    print(ex4)
    
    ex5 = {"a": 1} | {"a": 3, "b": 2}
    print(ex5)

print("\n")
print("#### binary operators ###")
binary_operators()
print("#### binary operators ###")
print("\n")