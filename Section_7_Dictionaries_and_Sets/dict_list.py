available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = []
while current_choice != 0:
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)
            print(f"Removing {chosen_part}")
        else:
            computer_parts.append(chosen_part)
            print(f"Adding {chosen_part}")
        print(computer_parts)
    elif current_choice == 0:
        break
    else:
        print("Please choose an option from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")
