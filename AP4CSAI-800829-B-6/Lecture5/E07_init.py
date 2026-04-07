import math

# Define a Point class with position and distance behavior
class Point:
    
    # Constructor: initialize a new Point with x and y
    def __init__(self, x, y):
        self.move(x, y)

    # Move the point to a new location
    def move(self, x, y):
        self.x = x
        self.y = y

    # Reset the point to the origin (0, 0)
    def reset(self):
        self.move(0.0, 0.0)

    # Compute the distance to another Point object
    def calculate_distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    

# Create a point at (3, 5)
point = Point(3, 5)
print(point.x, point.y)