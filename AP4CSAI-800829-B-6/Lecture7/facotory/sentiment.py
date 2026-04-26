class SentimentAnalyzer:
    def predict(self, text):
        return "positive" if "good" in text.lower() else "negative"