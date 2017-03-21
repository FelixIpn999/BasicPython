class Contact_List(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts




class Contacts:
    all_contacts = Contact_List()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class Friend(Contacts):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


class Suplier(Contacts):
    def order(self, order):
        print("If this were a real system we would send"
              "{} order to {}".format(order, self.name)
              )
