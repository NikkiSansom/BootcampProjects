# Practical Task 14 - Holiday Calculator

print("\nWelcome to the Holiday Calculator!\n")

# User chooses a flight destination
# Loop this section until a valid option from the preprogrammed list has been selected
destination_dictionary = {"1": "Paris",
                      "2": "Berlin",
                      "3": "Madrid"}
while True:
    city_flight = input("Please input a number to select your flight destination:\n"
                    "1: Paris\n"
                    "2: Berlin\n"
                    "3: Madrid\n")
    if city_flight in destination_dictionary:
        print(f"You have selected {destination_dictionary[city_flight]}.")
        continue_option = input("Confirm Selection?: Y/N\n")
        continue_option = continue_option.upper()
        if continue_option == "Y":
            break
        elif continue_option == "N":
            continue
        else:
            print("\nSorry! That wasn't a valid input. Please try again.\n")
            continue  
    else:
        print("\nSorry! That wasn't a valid input. Please enter whole numbers.\n")
        continue

# User inputs length of holiday
# Loop this section until user enters a whole number
# Convert the number of nights into a float for future calculations
while True:
    num_nights = (input("How many nights are you staying?: "))
    try:
        integer_check =  int(num_nights)
        break
    except ValueError:
        print("\nSorry! That wasn't a valid input. Please enter whole numbers.\n")
        continue
num_nights = float(num_nights)

# User selects car hire option
# Loop this section until either car hire is rejected or valid number of days entered
# Convert the number of days of hire into a float for future calculations
while True:
    car_option = input("Will you require car hire during your holiday?: Y/N\n")
    car_option = car_option.upper()
    if car_option == "Y":
            while True:
                rental_days = (input("How many days will you require a car for?: "))
                try:
                    integer_check =  int(rental_days)
                    break
                except ValueError:
                    print("\nSorry! That wasn't a valid input. Please enter whole numbers.\n")
                    continue
            rental_days = float(rental_days)
            break
    elif car_option == "N":
            rental_days = 0
            break
    else:
            print("\nSorry! That wasn't a valid input. Please try again.\n")
            continue

# Calculates total hotel cost by multiplying hotel cost (different epending on city destination)
# by number of nights staying
def hotel_cost(num_nights):
    if city_flight == "1":
        hotel_room = 100.00
    elif city_flight == "2":
        hotel_room = 82.00
    elif city_flight == "3":
        hotel_room = 67.00
    hotel = round(num_nights * hotel_room, 2) 
    return hotel

# Returns cost of flights based on user-defined destination
def plane_cost(city_flight):
    if city_flight == "1":
        flight_price = 37.50
    elif city_flight == "2":
        flight_price = 47.88
    elif city_flight == "3":
        flight_price = 55.55
    return flight_price

# Multiples car rental rate per day by number of days user defined
def car_rental(rental_days):
    days = round(rental_days * 29.95, 2)
    return days

# Calculates total holiday cost by adding separate hotel, flights and car rental costs
def holiday_cost(hotel_cost, plane_cost, car_rental):
    whole_total = round(hotel_cost + plane_cost + car_rental, 2)
    return whole_total

# Calculating the components of the holiday total
hotel_total = hotel_cost(num_nights)
flight_total = plane_cost(city_flight)
car_total = car_rental(rental_days)

total_holiday_cost = holiday_cost(hotel_total, flight_total, car_total)

print(f"\nFlights = £{flight_total}")
print(f"Hotel = £{hotel_total}")
print(f"Car Hire = £{car_total}")
print("In total, your holiday will cost £" + str(total_holiday_cost))
print("\nThank you for using the Holiday Calculator!")