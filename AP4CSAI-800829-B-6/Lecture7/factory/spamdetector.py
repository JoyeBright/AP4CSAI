class SpamDetector:
    def predict(self, text):
        return "spam" if "free" in text.lower() else "not spam"