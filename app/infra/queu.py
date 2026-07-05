from qstash import QStash

class QueueService:
 
    def __init__(self, token):
        self.client = QStash(token)

    def get_queue(self):
        return self.client