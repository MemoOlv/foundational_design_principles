from src.dependency_injection import MessageService, EmailSender

def test_messager_service():
    email_service = MessageService(EmailSender())
    obtained = email_service.send_message("Hello via Email")
    expected_email_message = "Sending mail: Hello via Email"
    assert obtained == expected_email_message

