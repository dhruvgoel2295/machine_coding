from .queue_u import QueueU
import threading

class Subscriber(object):
    def __init__(self, sid):
        self.sid = sid
        self.new_messages = QueueU()
        self.done = False
        self.lock = threading.RLock()
    
    def is_last_received(self):
        with self.lock:
            value = self.done
        return value

    def set_last_received(self, value=False):
        with self.lock:
            self.done = value

    def get_id(self):
        return self.sid

    def listen_for_messages(self):
        print("Listening")
        while (not self.is_last_received()) or (self.new_messages.length() > 0):
            message_len = self.new_messages.length()
            if message_len == 0:
                continue
            message = self.new_messages.pop()
            print("%s %s" % (message, self.sid))
        print("Subscriber: %s Finished." % self.sid)


    def receive_message(self, message, last=False):
        self.new_messages.push(message)
        self.set_last_received(last)


