# Define a Point class with a method that changes its state
class Point:
    # Method that resets the point to the origin
    def reset(self):
        self.x = 0
        self.y = 0

# Create two Point objects
p1 = Point()
p2 = Point()

# Assign coordinates to each object
p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

# Print the initial state of both points
print(p1.x, p1.y)
print(p2.x, p2.y)

# Call a method that modifies p1's attributes
p1.reset()
print("-----")

# Print the state after resetting p1
print(p1.x, p1.y)
print(p2.x, p2.y)
