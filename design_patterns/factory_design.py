# Factory Design Pattern Example in Python
class EmailNotification:
    def send(self, message):
        return f"Email notification sent with message: {message}"

class SMSNotification:
    def send(self, message):
        return f"SMS notification sent with message: {message}"
    
class AppNotification:
    def send(self, message):
        return f"App notification sent with message: {message}"
    
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "app":
            return AppNotification()
        else:
            raise ValueError(f"Invalid notification type: {notification_type}")
        
# Example usage
if __name__ == "__main__":
    factory = NotificationFactory()
    
    email_notification = factory.create_notification("email")
    print(email_notification.send("Hello via Email!"))
    
    sms_notification = factory.create_notification("sms")
    print(sms_notification.send("Hello via SMS!"))
    
    app_notification = factory.create_notification("app")
    print(app_notification.send("Hello via App!"))