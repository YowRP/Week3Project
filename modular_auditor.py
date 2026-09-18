def get_valid_input():
    while True:
        user_input = input("Please enter the stock quantity: ")
        # check for quit first
        if user_input.lower() == "quit" or user_input.lower() == "q":
            return None
        
        # check for valid non-negative integer
        if not user_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
    
        # if invalid, print message and continue looping
        # if valid, return it
        if user_input.isdigit():
            return int(user_input)
        

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total    

def calculate_tax(amount):
    tax_rate = 0.1
    return amount * tax_rate

def generate_report(total_units, failed_attempts):
    print("Total units will be : " + str(total_units))
    print("Failed attempts : " + str(failed_attempts))

def main() :
    total_units = 0
    failed_attempts = 0
    deliveries_processed = 0
    while True:
        user_input = get_valid_input()
        if user_input is None:
            break
        else:
            total_units = process_delivery(total_units, user_input)
            tax = calculate_tax(user_input)
            deliveries_processed += 1

    generate_report(total_units, failed_attempts)


