class Contact:
    def __init__(self, name, phone_no, gender, email_addr, postal_addr):
        self.name = name
        self.phone_no = phone_no
        self.gender = gender
        self.email_addr = email_addr
        self.postal_addr = postal_addr

if __name__ == "__main__":
    name = str(raw_input("Enter your Name:"))
    phone_no = int(raw_input("Enter your phone number:"))
    gender = str(raw_input("Enter your gender:"))
    email_addr = str(raw_input("Enter your email address:"))
    postal_addr = str(raw_input("Enter your postal address:"))






