# Base class
class Piece:
    def __init__(self, color):
        self.color = color

    def move(self):
        print("This piece has no defined movement")


# Subclass: Rook
class Rook(Piece):
    def move(self):
        print("Rook moves in straight lines")


# Subclass: Bishop
class Bishop(Piece):
    def move(self):
        print("Bishop moves diagonally")


# Create objects
r = Rook("white")
b = Bishop("black")

r.move()
b.move()