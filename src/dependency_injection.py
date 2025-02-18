class MessageService:
    def __init__(self, sender):
        self.sender = sender
    def send_message(self, message: str):
        return self.sender.send(message)

class EmailSender:
    def send(self, message: str):
        return f"Sending mail: {message}"
    
class SMSSender:
    def send(self, message: str):
        return f"Sending SMS: {message}"
