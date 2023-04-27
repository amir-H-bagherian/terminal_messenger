from datetime import date
import uuid

class Message:
    
    def __init__(self, sender, receiver, title, content=None, date=date.today(), is_read=False):
        self.message_id = uuid.uuid4()
        self._sender = sender
        self._receiver = receiver
        self.title = title
        self.content = content
        self.date = date
        self.is_read = is_read
        self.mail_box = None
    
    def mark_as_read(self):
        self.is_read = True