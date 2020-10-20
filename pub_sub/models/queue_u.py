import threading

class QueueU(object):
    def __init__(self):
        self.data = []
        self.lock = threading.RLock()

    def push(self, item):
        with self.lock:
            self.data.append(item)

    def pop(self):
        with self.lock:
            item = self.data.pop(0)
        return item

    def length(self):
        with self.lock:
            length = len(self.data)
        return length
