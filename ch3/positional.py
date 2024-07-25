
def concatenate(first: str, second: str, delim: str):
    return delim.join([first,second])

print(concatenate("test", "test2", delim=" put this in "))

def concatenate2(*items, delim: str):
    return delim.join(items)

print(concatenate2("str1", "str2", "str3", delim=" in between "))
