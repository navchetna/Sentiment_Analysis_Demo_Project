from sklearn.datasets import fetch_20newsgroups
from bertopic import BERTopic


class BERTopicModel:
    def __init__(self):
        self.model = BERTopic()

    def fetch_dataset(self):
        docs = fetch_20newsgroups(subset="all", remove=('headers', 'footers', 'quotes'))["data"]
        print('Data fetched successfully!')
        return docs

    def get_topic_info(self, docs):
        self.topics, self.probs = self.model.fit_transform(docs)
        topic_info = self.model.get_topic_info()
        
        return topic_info
