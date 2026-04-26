# This is your context
# here we store extrinsic/unique data and references a shared token

class Context:
    def __init__(self, token, position):
        self.token = token
        self.position = position
    
    # helper
    def display(self):
        self.token.display(self.position)