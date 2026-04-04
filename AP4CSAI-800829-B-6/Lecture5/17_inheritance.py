from E16_abstract import Piece

class Pawn(Piece):  # Pawn inherits from Piece
    def move(self, board, to):
        print("Pawn moves forward")


class Rook(Piece):  # Rook inherits from Piece
    def move(self, board, to):
        print("Rook moves in straight lines")

