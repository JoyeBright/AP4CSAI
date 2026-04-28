# This is your client

from factory import Factory
from context import Context

sentence = "code after code I write code to fix code"

words = sentence.split()

factory = Factory()
occurrences = []

for position, word in enumerate(words):
    shared_token = factory.get_token(word)
    occurrence = Context(shared_token, position)
    occurrences.append(occurrence)


# factory.show_cache()
# print("\nToken occurrences:")
# for occurrence in occurrences:
#     occurrence.display()
