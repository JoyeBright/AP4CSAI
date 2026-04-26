from E00_aimodels import TranslationModel, SentimentModel

class ImageClassifier:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "I classify images."

m1 = TranslationModel("XGLM")
m2 = SentimentModel("BERT")
m3 = ImageClassifier("CNN")

# Type Checking

# def print_role(model):
#     if isinstance(model, TranslationModel):
#         return model.get_role()

#     elif isinstance(model, SentimentModel):
#         return model.get_role()
    
#     elif isinstance(model, ImageClassifier):
#         return model.get_role()

# Polymorphism

def print_role(model):
    return model.get_role()

print(print_role(m1))
print(print_role(m2))
print(print_role(m3))