import random

while True:
    print("Welcome to the CSULB Water Billing System")
    account_number = random.randint(1000, 9000)  # Generate a random account number
    name = input("Enter Customer Name: ")
    address = input("Enter Address: ")
    phone_number = input("Enter Phone Number: ")

    while True:
        customer_code = input("Enter Customer Code (R, C, or I): ").upper()
        if customer_code in ('R', 'C', 'I'):
            break
        else:
            print("Invalid input. Please enter a valid customer code.")

    # Input validation for meter readings
    valid_readings = False
    while not valid_readings:
        beginning_reading = input("Enter Beginning Meter Reading (between 0 and 999999999): ")
        ending_reading = input("Enter Ending Meter Reading (between 0 and 999999999): ")

        if beginning_reading.isdigit() and ending_reading.isdigit():
            beginning_reading = int(beginning_reading)
            ending_reading = int(ending_reading)
            if 0 <= beginning_reading <= 999999999 and 0 <= ending_reading <= 999999999:
                valid_readings = True
            else:
                print("Invalid input. Readings should be within the specified range.")
        else:
            print("Invalid input. Please enter valid meter readings.")

    rate = 0.0  # Initialize rate with 0.0
    base_charge = 0.0  # Initialize base_charge with 0.0

    if customer_code == 'R':
        rate = 0.0005
        base_charge = 5.00
    elif customer_code == 'C':
        if ending_reading <= 4000000:
            rate = 0.00025
            base_charge = 1000.00
        else:
            rate = 0.00025
            base_charge = 1000.00 + (ending_reading - 4000000) * 0.00025
    elif customer_code == 'I':
        if ending_reading <= 4000000:
            base_charge = 1000.00
        elif 4000000 < ending_reading <= 10000000:
            base_charge = 2000.00
        else:
            base_charge = 2000.00 + (ending_reading - 10000000) * 0.00025

    if ending_reading < beginning_reading:
        ending_reading += 1000000000  # Handle meter rollover
    gallons_used = (ending_reading - beginning_reading) / 10.0
    amount_billed = base_charge + gallons_used * rate

    # Print the bill
    print("\n======================== Bill =========================")
    print(f"Account Number: {account_number}")
    print(f"Customer Name: {name}")
    print(f"Address: {address}")
    print(f"Phone Number: {phone_number}")
    print(f"Customer Code: {customer_code}")
    print(f"Beginning Meter Reading: {beginning_reading:09d}")
    print(f"Ending Meter Reading: {ending_reading:09d}")
    print(f"Gallons of Water Used: {gallons_used:.1f}")
    print(f"Amount Billed: ${amount_billed:.2f}")
    print("=======================================================\n")

    again = input("Do you want to perform a new calculation? (y/n): ").lower()
    if again != 'y':
        break

print("Thank you for using the CSULB Water Billing System. Goodbye!")
