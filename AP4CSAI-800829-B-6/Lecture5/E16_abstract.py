import abc  # Abstract base class support

class Piece(abc.ABC):  # Abstract class (cannot be instantiated because it contains abstract methods)
    def __init__(self, set, color, shape):
        self.chess_set = set
        self.color = color
        self.shape = shape
    
    @abc.abstractmethod  # Must be implemented by subclasses
    def move(self, board, to):
        pass  # No implementation here