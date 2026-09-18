def get_valid_input():
    failed_attempts = 0
    while True:
        user_input = input("Please enter the stock quantity: ")
        if user_input.lower() == "quit" or user_input.lower() == "q":
            return None, failed_attempts
        
        if not user_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            failed_attempts += 1
            continue

        if user_input.isdigit():
            return int(user_input), failed_attempts
        
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total    

def calculate_tax(amount):
    tax_rate = 0.1
    return amount * tax_rate


