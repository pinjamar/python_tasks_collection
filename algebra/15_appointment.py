class Appointment:
    def __init__(self, title, start_time, end_time):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Title: {self.title}\nStart Time: {self.start_time}\nEnd Time: {self.end_time}"