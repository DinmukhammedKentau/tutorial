class PhoneBook:
    def __init__(self,first_name,last_name,phone_number):
      self.id=None
      self.first_name = first_name
      self.last_name = last_name
      self.phone_number=phone_number
    def __repr__(self):
        return f"{self.first_name} {self.last_name} : {self.phone_number}"
