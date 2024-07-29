class Point:
    x: int
    y: int
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def where_is_point(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

# Create an instance of Point
point = Point(0, 0)  # Or any other x and y values you want

# Call the function with the Point instance
where_is_point(point=point)