# Prompt user to enter current hour in military time
current_hour = int(input("Enter the current hour (24-Hour Clock format): "))

# Prompt user to enter the number of hours to wait for the alarm
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Check for invalid input for current_hour
if current_hour < 0 or current_hour > 23:
    print("Invalid input for current. Please enter a number between 0 and 23.")
else:
    # Calculate number of days and new alarm hour
    days_to_wait = hours_to_wait // 24
    new_hour = (current_hour + hours_to_wait) % 24

    # Change number of days if necessary
    if new_hour < current_hour:
        days_to_wait += 1

    # Print final message
    print(f"The alarm will sound in {days_to_wait} day(s) at {new_hour} hour(s).")

def calculate_water_bill():
    # Get the customer code, starting meter, and ending meter from the user
    customer_code = input("Enter the customer's code (R for Residential, C for Commercial, I for Industrial): ").upper()
    starting_meter = int(input("Enter the customer's beginning meter reading: "))
    ending_meter = int(input("Enter the customer's ending meter reading: "))

    # Check to make sure for valid meter readings
    if 0 <= starting_meter <= 999999999 and 0 <= ending_meter <= 999999999:
        # Calculate the gallons used
        if starting_meter <= ending_meter:
            gallons_used = (ending_meter - starting_meter) / 10.0
        else:
            gallons_used = (1000000000 - starting_meter + ending_meter) / 10.0

        # Calculate the bill using the customer code and gallons used
        if customer_code == 'R':
            bill = 5.00 + 0.0005 * gallons_used
        elif customer_code == 'C':
            if gallons_used <= 4000000:
                bill = 1000
            else:
                bill = 1000 + 0.00025 * (gallons_used - 4000000)
        elif customer_code == 'I':
            if gallons_used <= 4000000:
                bill = 1000
            elif 4000000 < gallons_used <= 10000000:
                bill = 2000
            else:
                bill = 2000 + 0.00025 * (gallons_used - 10000000)
        else:
            print("Invalid customer code")
            return

        # Output the customer code and bill amount
        print("\nCustomer code:", customer_code)
        print("Beginning meter reading: {:0>9}".format(starting_meter))
        print("Ending meter reading: {:0>9}".format(ending_meter))
        print("Gallons of water used: {:.2f}".format(gallons_used))
        print("Amount billed: ${:.2f}".format(bill))
    else:
        print("Invalid meter reading")

if __name__ == '__main__':
    calculate_water_bill()
