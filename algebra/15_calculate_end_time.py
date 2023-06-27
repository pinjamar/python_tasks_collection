from datetime import timedelta

def calculate_end_time(start, duration_in_hours):
    return start + timedelta(hours=duration_in_hours)