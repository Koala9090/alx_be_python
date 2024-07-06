from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    days = int(input("Enter the number of days to add: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(hours=days)
    print(f"Date after {days} days: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()