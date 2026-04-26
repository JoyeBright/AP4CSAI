from E00_aimodels import TranslationModel, SentimentModel

m1 = TranslationModel("XGLM")
m2 = SentimentModel("BERT")

def print_role(model):
    if isinstance(model, TranslationModel):
        return model.get_role()

    elif isinstance(model, SentimentModel):
        return model.get_role()

print(print_role(m1))
print(print_role(m2))
