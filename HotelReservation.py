from datetime import datetime
import locale


print("The Hotel Reservation Program\n")

again="y"

#arrival date

while again.lower()== "y":
    while True:
        date_str = input("Enter arrival date(YYYY-MM-DD): ")
        try:
            arrival_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again. ")
            print()
            continue

        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if arrival_date < today:
            print("Arrival date must be today or later. Try again.")
            print()
        else:
            break

 
#departure date

    while True:
        date_str = input("Enter departure date(YYYY-MM-DD): ")
        try:
           departure_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
           print("Invalid date format. Please try again. ")
           print()
           continue

        if departure_date <= arrival_date:
           print("Depature date must be after arrival date. Please try again.")
           print()
        else: 
           break

    print()

    rate = 85.0
    rate_message =""
    if arrival_date.month == 8: 
        rate = 105.0
        rate_message = "(High season)"
    total_nights = (departure_date - arrival_date).days
    total_cost = rate * total_nights

    date_format= "%B %d, %Y"
    locale.setlocale(locale.LC_ALL, "en_US")
    print(f"Arrival Date: {arrival_date:{date_format}}")
    print(f"Departure Date: {departure_date: {date_format}}")
    print(f"Nightly rate: {locale.currency(rate)} {rate_message}")
    print(f"Total night:  {total_nights}")
    print(f"Total prices: {locale.currency(total_cost)}")
    print()

    again= input ("Continue? (y/n): ")
    print()


print('Bye!')





   