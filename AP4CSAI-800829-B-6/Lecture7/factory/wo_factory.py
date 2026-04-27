from sentiment import SentimentAnalyzer
from spamdetector import SpamDetector
from topicclassifier import TopicClassifier

# Object creation is exposed in your main file

def run_task(task, text):
    if task == "sentiment":
        model = SentimentAnalyzer()
    elif task == "spam":
        model = SpamDetector()
    elif task == "topic":
        model = TopicClassifier()
    else:
        raise ValueError("Unknown task")

    return model.predict(text)