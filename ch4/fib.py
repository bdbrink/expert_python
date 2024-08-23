
def fibonacci():
    a,b = 0,1
    while True:
        yield b
        a, b = b, a + b

for item in fibonacci():
    print(item)
    if item > 10:
        break
