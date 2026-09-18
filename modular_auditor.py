inventory = 0
rejected_entries = 0
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
    