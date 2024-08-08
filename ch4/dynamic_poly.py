import os

files = [f for f in os.listdir() if os.path.isfile(f)]

def printfile(file):
    try:
        contents = file.read()
        print(contents)
    finally:
        file.close()

for filename in files:
    with open(filename, 'r') as file:
        printfile(file)
