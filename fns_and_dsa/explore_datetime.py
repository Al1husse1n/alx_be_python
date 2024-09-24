from datetime import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.today()
    print(current_date)

def calculate_future_date():
    days_added = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.today()
    future_date = current_date + timedelta(days = days_added) 
    print(future_date)
