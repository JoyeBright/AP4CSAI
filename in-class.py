class TranslationModel:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "I translate textual information."

class SentimentModel:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "I analyze the sentiment of text."

t1 = TranslationModel("XGLM")
s1 = SentimentModel("BERT")

def print_role(model):
    if isinstance(model, TranslationModel):
        return model.get_role()
    elif isinstance(model, SentimentModel):
        return model.get_role()
    
print(print_role(t1))
print(print_role(s1))