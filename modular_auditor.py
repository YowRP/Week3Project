inventory = 0
rejected_entries = 0
while True:
    user_input = input("Please enter the stock quantity")
    
    if not user_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        rejected_entries += 1
        continue

    elif int(user_input) < 0:
        print("Invalid input. Please enter a non-negative number.")
        rejected_entries += 1
        continue
    
    inventory += int(user_input)

    if inventory > 500 :
            print("ALERT! Stock quantity has reached or exceeded 500 units.")
            break

    user_end = input("Do you want to add more stock? (yes/no): ")
    if user_end.lower() == "no" or user_end.lower() == "n":
        break
    else:
        continue


print ("Total stock quantity:", inventory)
print ("Total rejected entries:", rejected_entries)

inventory = 0
rejected_entries = 0
def get_valid_input():
    while True:
         user_input = input("Please enter the stock quantity: ")
         if not user_input.isdigit():
             print("Invalid input. Please enter a valid number.")
             rejected_entries += 1
             continue
         elif int(user_input) < 0:
             print("Invalid input. Please enter a non-negative number.")
             rejected_entries += 1
             continue
         return int(user_input) and rejected_entries

def process_delivery(user_input, inventory):

    get_valid_input(user_input)
    inventory += user_input
    user_end = input("Do you want to add more stock? (yes/no): ")
    if user_end.lower() == "no" or user_end.lower() == "n":
        return inventory
    else:
        return get_valid_input()

def calculate_tax_amount(inventory):
    tax_rate = 0.1
    tax_amount = inventory * tax_rate
    return tax_amount

def general_report(total_units, failed_attempts):
    total_units = inventory
    failed_attempts = rejected_entries
    print("Total stock quantity:", total_units)
    print("Total rejected entries:", failed_attempts)
    
    