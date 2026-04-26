# this is your flyweight
# here we store only intrinsic/shared data
# shared data in our problem: text, its id, and length

class Flyweight:
    def __init__(self, text, token_id):
        self.text = text
        self.token_id = token_id
        self.length = len(text)
    
    # helper
    def display(self, position):
        print(
            f"Token '{self.text}' "
            f"(id={self.token_id}, length={self.length}) "
            f"at position {position}"
        )
