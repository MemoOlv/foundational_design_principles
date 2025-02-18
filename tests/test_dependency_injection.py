from src.dependency_injection import MessageService, EmailSender, SMSSender

def test_messager_service():
    email_service = MessageService(EmailSender())
    obtained = email_service.send_message("Hello via Email")
    expected_email_message = "Sending mail: Hello via Email"
    assert obtained == expected_email_message

    sms_service = MessageService(SMSSender())
    obtained = sms_service.send_message("Hello via SMS")
    expected_sms_message = "Sending SMS: Hello via SMS"
    assert obtained == expected_sms_message

