def main():
    time_str = input("Enter the time in 24-hour format (HH:MM): ")
    time = convert(time_str)

    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")

def convert(time):


    try:
        hours, minutes = map(int, time.split(':'))
        return hours + minutes / 60.0
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM.")
        return 0.0

if __name__ == "__main__":
    main()
