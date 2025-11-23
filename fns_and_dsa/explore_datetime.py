from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Print in "YYYY-MM-DD HH:MM:SS" format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.now()
    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)
    # Print in "YYYY-MM-DD" format
    print("Future date:", future_date.strftime("%Y-%m-%d"))


def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Prompt user and calculate future date
    days_input = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days_input)


if __name__ == "__main__":
    main()
