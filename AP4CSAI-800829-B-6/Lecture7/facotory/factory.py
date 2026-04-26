from sentiment import SentimentAnalyzer
from spamdetector import SpamDetector
from topicclassifier import TopicClassifier

# --- Factory ---
class NLPFactory:
    @staticmethod
    def create(task):
        if task == "sentiment":
            return SentimentAnalyzer()
        elif task == "spam":
            return SpamDetector()
        elif task == "topic":
            return TopicClassifier()
        else:
            raise ValueError("Unknown task")

def run_task(task, text):
    model = NLPFactory.create(task)
    return model.predict(text)

def main():
    text = "Python is a good programming language"

    print("Sentiment:", run_task("sentiment", text))
    print("Spam:", run_task("spam", text))
    print("Topic:", run_task("topic", text))

if __name__ == "__main__":
    main()

