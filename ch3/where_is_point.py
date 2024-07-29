## need to specify x and y without match args
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
point = Point(0, 1)  # Or any other x and y values you want

# Call the function with the Point instance
where_is_point(point=point)

## In this example no need to specify x and y as the match args does that
class Point2:
    x: int
    y: int
    
    __match_args__ = ("x", "y")
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def where_is_point2(point2):
    match point2:
        case Point2(0, 0):  # Using positional syntax
            print("Origin")
        case Point2(0, y):
            print(f"Y={y}")
        case Point2(x, 0):
            print(f"X={x}")
        case Point2():
            print("Somewhere else")
        case _:
            print("Not a point")

# Create an instance of Point2
point2 = Point2(0, 1) 

# Call the function with the Point2 instance
where_is_point2(point2)