from src.dependency_injection import MessageService, EmailSender

def test_messager_service():
    email_service = MessageService(EmailSender())
    email_message = "Hello via Email"
    obtained = email_service.send_message(email_message)
    assert obtained == email_message

