class notification:
    def send(self):
        print("notification sent")

class emailnotification(notification):
    def __init__(self):
        print("email sent")

class smsnotification(notification):
    def send(self):
        print("sms sent")