class TranslationModel:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "I translate text."
    
class SentimentModel:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "I analyze sentiment."
