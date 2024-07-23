from collections import ChainMap

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
    
    # only thing common among all 3 is 1
    ex1 = {1,2,3} & {1,4} & {1,2,3,4,5}
    print(ex1)
    
    ex2 = {1,2,3} | {1,4}
    print(ex2)
    
    ex3 = {1,2,3} - {1,4}
    print(ex3)
    
    ex4 = {1,2,3} ^ {1,4}
    print(ex4)
    
    ex5 = {"a": 1} | {"a": 3, "b": 2}
    print(ex5)
    
    new_dict = {"a": 1}
    new_dict |= {"a":7, "b": 11}
    print(new_dict)
    
    a = {"a": 1}
    b = {"a": 3, "b": 2}
    
    print({**a, **b})

print("\n")
print("#### binary operators ###")
binary_operators()
print("#### binary operators ###")
print("\n")

def chain_map():
    
    user_account = {"iban": "gb71barc20031885581746", "type": "account"}
    user_profile = {"display_name": "John Doe", "type": "profile"}
    user = ChainMap(user_account, user_profile)
    print(user["iban"])
    print(user["display_name"])
    print(user["type"])
    print(user)
    
    user_profile["display_name"] = "new name"
    print(user)
    
    # only CRUD left most mappings
    user["display_name"] = "John guy"
    user["age"] = 18
    user["type"] = "extension"
    print(user_profile)
    print(user_account)

print("\n")
print("#### using chainmap to unpack dict ###")
chain_map()
print("#### using chainmap to unpack dict ###")