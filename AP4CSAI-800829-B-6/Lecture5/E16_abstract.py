import abc

class Piece(abc.ABC):
    def __init__(self, set, color, shape):
        self.chess_set = set
        self.color = color
        self.shape = shape
    
    @abc.abstractmethod
    def move(self, board, to):
        pass

