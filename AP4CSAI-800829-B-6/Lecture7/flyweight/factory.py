# this is your factory
# factory manages the flyweight objects
# basically it reuses objects if they already exists

from flyweight import Flyweight

class Factory:
    def __init__(self):
        self._tokens = {}
        self._next_id = 1

    def get_token(self, text):
        key = text.lower()

        if key not in self._tokens:
            print (f"Creating shared token: {key}")
            self._tokens[key] = Flyweight(key, self._next_id)
            self._next_id +=1
        else:
            print(f"Reusing shared token: {key}")

        return self._tokens[key]
    
    # helper
    def show_cache(self):
        print("\Shared tokens stored in factory")
        for token_text, token in self._tokens.items():
            print(f"- {token_text}: id={token.token_id}")

        print(f"Total shared Token objects: {len(self._tokens)}")

        