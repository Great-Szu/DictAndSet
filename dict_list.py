available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
shopping_cart = []

while current_choice != "0":
    if current_choice in available_parts:

        if available_parts[current_choice] in shopping_cart:
            shopping_cart.remove(available_parts[current_choice])
            print("Your cart contain: ", shopping_cart)

        else:
            shopping_cart.append(available_parts[current_choice])
            print("Your cart contain: ", shopping_cart)

    else:
        print("Choose an item from a list to add")
        print("Your cart contain: ", shopping_cart, "\n")
        for key, value in available_parts.items():
            print(key, value, sep=" - ")

    current_choice = input("> ")