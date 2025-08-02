class phone:
    def __init__(self,owner_name):
        self.owner_name = owner_name

    def call_contact(self,contact_name):
        print(f"calling {contact_name}... please wait.")

        print(f"{contact_name} is now on call")
    
    def take_picture(self):
        print("opening camera...")
        print("picture taken and saved to gallery.")


my_phone = phone("lakshmi")
my_phone.call_contact("bossu")
my_phone.take_picture()

        