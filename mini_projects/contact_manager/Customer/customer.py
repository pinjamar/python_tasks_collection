class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def print_customer_data(self):
        return f'Name: {self.name}\tEmail: {self.email}\n'