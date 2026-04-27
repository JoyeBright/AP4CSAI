class TopicClassifier:
    def predict(self, text):
        text = text.lower()
        if "python" in text:
            return "technology"
        elif "football" in text:
            return "sports"
        return "general"
