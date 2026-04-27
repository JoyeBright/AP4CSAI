class AiModel:
    def get_role(self):
        pass

class TranslationModel(AiModel):
    def get_role(self):
        return "I translate text."
    
class SentimentModel(AiModel):

    def get_role(self):
        return "I analyze sentiment."

class ImageClassifier(AiModel):

    def get_role(self):
        return "I classify images."

m1 = TranslationModel("XGLM")
m2 = SentimentModel("BERT")
m3 = ImageClassifier("CNN")

# Inheritance-based polymorphism

def print_role(model):
    return model.get_role()

print(print_role(m1))
print(print_role(m2))
print(print_role(m3))