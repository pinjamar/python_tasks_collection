class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.appointments = []

    def __str__(self):
        return f"Name: {self.name} Email: {self.email}"
    
    def add_appointment(self, appointment):
        self.appointments.append(appointment)
    
    def get_appointments(self):
        return self.appointments