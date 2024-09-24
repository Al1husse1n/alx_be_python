from datetime import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_datetime)

def calculate_future_date():
    days_added = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    future_date = formatted_datetime + timedelta(days = days_added) 
    print(future_date)
