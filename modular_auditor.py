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

