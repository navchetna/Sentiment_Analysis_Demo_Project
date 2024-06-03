from main import BERTopicModel

if __name__ == "__main__":
    model = BERTopicModel()
    docs = model.fetch_dataset()
    
    topic_info = model.get_topic_info(docs)
    print(topic_info)
