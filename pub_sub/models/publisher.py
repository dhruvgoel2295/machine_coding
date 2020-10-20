from .queue_u import QueueU
from services.publisher_service import PublisherService
import threading

class Publisher(object):
    def __init__(self, topic):
        self.topic = topic
        self.message_queue = QueueU()
        self.service = PublisherService()
        self.lock = threading.RLock()
        self.subscribers = {}
        self.done = False
    
    
    def is_last_sent(self):
        with self.lock:
            value = self.done
        return value

    def set_last_sent(self, value=False):
        with self.lock:
            self.done = value

    def publish_message(self, message, last=False):
        self.message_queue.push("%s: %s"% (self.topic, message))
        self.set_last_sent(last)

    def push_messages(self):
        while (not self.is_last_sent()) or (self.message_queue.length() > 0):
            last = False
            message_len = self.message_queue.length()
            if message_len == 0:
                continue
            if self.is_last_sent() and self.message_queue.length() == 1:
                last = True
            message_to_push = self.message_queue.pop()
            self.service.push_to_sibscribers(message_to_push, self.subscribers, last)
        print("Publisher is done.")

    def add_subscriber(self, sid, subscriber):
        self.subscribers[sid] = subscriber


