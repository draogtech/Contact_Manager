class Contact:
    def __init__(self, name, phone_no, gender, email_addr, postal_addr):
        self.name = name
        self.phone_no = phone_no
        self.gender = gender
        self.email_addr = email_addr
        self.postal_addr = postal_addr

    def __repr__(self):
        return "{}, {}, {}, {}, {}".format(self.name, self.phone_no, self.gender, self.email_addr, self.postal_addr)


class Manager:
    def __init__(self, contact_list=[]):
        self.contact_list = contact_list

    def __confirm(self, action):
        self.action = action
        # Ask the user if they'd like to proceed with action. Return True if yes, otherwise False
        action = raw_input("Do you want to proceed? Y or N: ")
        if action == 'y':
            return True
        else:
            return False

    def __repr__(self):
        formatted_entries = ""
        for entry in self.contact_list:
            formatted_entries += str(entry) + "\n"
        return "The contact List is: \n{}".format(formatted_entries)

    def add_contact(self):
        print("-------Add Contact--------")
        if not self.__confirm("Add Contact"):
            return False

        # prompt user for contact details
        new_contact = Contact(name=raw_input("Enter name:"), phone_no=raw_input("Enter phone no:"), gender=raw_input("Enter gender:"), email_addr=raw_input("Enter email:"), postal_addr=raw_input("Enter Postal Address"))
        self.contact_list.append(new_contact)
        print(new_contact)

    def delete_contact(self):
        print("------Delete Contact--------")
        if not self.__confirm("Add Contact"):
            return False
        phone_no = raw_input("Enter the phone no as key to search and delete:")
        for contact in self.contact_list:
            if phone_no == contact.phone_no:
                self.contact_list.remove(contact)
                print("{} has been deleted".format(contact))
            else:
                print("No match")

    def search_contact(self):
        print("------Search Contact--------")
        if not self.__confirm("Add Contact"):
            return False
        phone_no = raw_input("Enter the phone no as key to search:")
        for contact in self.contact_list:
            if phone_no == contact.phone_no:
                print("The contact details are: {} ".format(contact))
            else:
                print("No match")


if __name__ == "__main__":
    update = Manager()
    update.add_contact()
    update.add_contact()
    print(update)
    update.delete_contact()
    update.search_contact()






















