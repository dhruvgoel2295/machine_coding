from models.subscriber import Subscriber
import threading

class PublisherService(object):

    def subscribe(self, publisher, subscriber):
        publisher.add_subscriber(subscriber.get_id(), subscriber)

    def push_to_sibscribers(self, message, subscribers, last=False):
        for subscriberid, subscriber in subscribers.items():
            thread = threading.Thread(target=subscriber.receive_message, args=(message, last))
            thread.start()


