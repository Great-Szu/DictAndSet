from contents import pantry, recipes
from datetime import date

def create_shoppinglist(food_items: dict) -> str:
    """
    This program creates a txt file with shopping list
    with food_items, and it's quantity based on recipes
    and user output.

    :param food_items: dict with food_items and it's quantity missing
        for recipe
    :return: String with direction to the shopping list
    """
    today = str(date.today()) + ".txt"
    path = "C:/Users/panmi/IdeaProjects/DictAndSet/shopping_lists/" + today

    with open(path, 'a') as file:
        for item, quantity in food_items.items():
            file.write(f"{item}:\n {quantity}\n")
    return path

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}

for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display a meny of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")
    list_of_items_to_buy = {}
    dont_have_idea_for_name = {}

    if choice == "0":
        break

    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"\nYou have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)

        for value, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(value, 0)

            if required_quantity <= quantity_in_pantry:
                print(f"\t{value} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                dont_have_idea_for_name[value] = quantity_to_buy
                list_of_items_to_buy[selected_item] = dont_have_idea_for_name
                print(f"\tYou need to buy {quantity_to_buy} of {value}")

        print("\nCreating shopping list of missing ingredients...")
        create_shoppinglist(list_of_items_to_buy)
        print(f"Shopping list is here {create_shoppinglist(list_of_items_to_buy)}")