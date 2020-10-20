from models.queue_u import QueueU
import threading
from models.subscriber import Subscriber
from models.publisher import Publisher


class Driver(object):
    def __init__(self):
        self.publishers = {}
        self.subscribers = {}

    def create_topic(self, topic):
        self.publishers[topic] = Publisher(topic)

    def create_subscriber(self, subscriber_id):
        new_subscriber = Subscriber(subscriber_id)
        self.subscribers[subscriber_id] = new_subscriber
        return new_subscriber

    def subscribe_to_topic(self, topic, subscriber_id):
        self.publishers[topic].add_subscriber(subscriber_id, self.subscribers[subscriber_id])
        
    def push_to_topic(self, topic, message, last=False):
        self.publishers[topic].publish_message(message, last)

    def start_publishing(self):
        for publisherid, publisher in self.publishers.items():
            thread = threading.Thread(target=publisher.push_messages)
            thread.start()

    def start_subscribers(self):
        for subscriberid, subscriber in self.subscribers.items():
            thread = threading.Thread(target=subscriber.listen_for_messages)
            thread.start()

    def main(self):
        topic_1 = "python"
        topic_2 = "jave"
        sub1 = "s1"
        sub2 = "s2"
        sub3 = "s3"
        self.create_topic(topic_1)
        self.create_topic(topic_2)
        print("Topics Created")
        s1 = self.create_subscriber(sub1)
        s2 = self.create_subscriber(sub2)
        s3 = self.create_subscriber(sub3)
        print("Subs Created")
        self.subscribe_to_topic(topic_1, sub1)
        self.subscribe_to_topic(topic_2, sub1)
        self.subscribe_to_topic(topic_1, sub3)
        self.subscribe_to_topic(topic_2, sub2)
        print("Topics Subscribed")
        self.start_publishing()
        print("Publishers started")
        self.start_subscribers()
        print("Subscribers started")
        self.push_to_topic(topic_1, "python good")
        self.push_to_topic(topic_2, "java good")
        self.push_to_topic(topic_1, "python bad")
        self.push_to_topic(topic_1, "java bad")
        print("Messages pushed")
        self.push_to_topic(topic_1, "python bye", last=True)
        self.push_to_topic(topic_2, "java bye", last=True)
        print("Last Messages pushed")

driver_obj = Driver()
driver_obj.main() 
