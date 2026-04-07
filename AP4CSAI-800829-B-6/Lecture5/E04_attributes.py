# Define an empty class named Point
class Point:
    pass

# Create two Point objects
p1 = Point()
p2 = Point()

# Add attributes to the first object using dot notation
p1.x = 5
p1.y = 4

# Add attributes to the second object
p2.x = 3
p2.y = 6

# Print the attributes of each object
print(p1.x, p1.y)
print(p2.x, p2.y)

##########################
# Class attributes are defined in the class body
# They are shared by all instances of the class

# class Test:
#     x = 0
#     y = 10

# t1 = Test()
# t2 = Test()

# t1.x = 5  # creates an instance attribute for t1 only

# print(t1.x)  # 5  (instance attribute)
# print(t2.x)  # 0  (still class attribute)
