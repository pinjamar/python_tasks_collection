from datetime import datetime, timedelta
import os

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

class Appointment:
    def __init__(self, title, start_time, end_time):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Title: {self.title}\nStart Time: {self.start_time}\nEnd Time: {self.end_time}"

def get_date_and_time_parts(datetime_string):
    datetime_object = datetime.strptime(datetime_string, "%m/%d/%Y %H:%M")
    year = datetime_object.year
    month = datetime_object.month
    day = datetime_object.day
    hour = datetime_object.hour
    minute = datetime_object.minute

    return year, month, day, hour, minute

users = []

while True:
    print("--- Schedule Application ---")
    print("1. Enter a new user.")
    print("2. Add an appointment to an existing user.")
    print("3. Print all appointments for a user.")
    print("4. Exit the application")

    choice = input("Enter your choice (1, 2, 3 or 4): ")

    if choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("Enter user's name: ")
        email = input("Enter user's email: ")

        user = User(name, email)
        users.append(user)

    elif choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        if not users:
            print("No existing users. Please enter a new user first.")
            continue

        # Print existing users
        print("\n--- Existing Users ---")
        # Želimo isprintati u obliku 1. Filip Skendrovic filip.skendrovic@gmail.com
        i = 1
        for user in users: # Naša users lista je sačinjena od user objekata. 
            print(f"{i}. {user.name} ({user.email})") 
            i += 1

        # Naša lista users se sastoji od user objekata: [user1, user2]
        
        user_index = int(input("Enter the index of the user: ")) - 1

        if user_index < 0 or user_index >= len(users):
            print("Invalid user index!")
            continue

        user = users[user_index]
    
    elif choice == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        if not users:
            print("No existing users. Please enter a new user first.")
            continue

        # Print existing users
        print("\n--- Existing Users ---")
        # Želimo isprintati u obliku 1. Filip Skendrovic filip.skendrovic@gmail.com
        i = 1
        for user in users: # Naša users lista je sačinjena od user objekata. 
            print(f"{i}. {user.name} ({user.email})") 
            i += 1

        user_index = int(input("Enter the index of the user: ")) - 1

        if user_index < 0 or user_index >= len(users):
            print("Invalid user index!")
            continue

        user = users[user_index]

        # Print user's appointments
        print(f"\n--- Appointments for User: {user.name} ---")
        appointments = user.get_appointments()
        if not appointments:
            print("No appointments found for this user.")
        else:
            for appointment in appointments:
                print(appointment)
                print()
        input('Press ENTER to continue ')
        continue

    elif choice == '4':
        print("Exiting the Schedule Application")
        break
    else:
        print("Invalid choice. Please try again")
        continue

    # Appointments loop
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n--- Appointments ---")
        print("Enter 'q' to finish adding appointments for this user.")

        title = input("Enter appointment title: ")
        if title == 'q':
            break

        datetime_input = input("Enter appointment date and time in format (MM/DD/YYYY HH:MM): ")

        year, month, day, hour, minute = get_date_and_time_parts(datetime_input)

        # Create datetime objects for appointments
        start_time = datetime(year, month, day, hour, minute)
        duration = float(input("Enter duration of appointment in hours: "))
        end_time = start_time + timedelta(hours=duration)

        appointment = Appointment(title, start_time, end_time)

        # Add appointment to the user
        user.add_appointment(appointment)