from contents import pantry, recipes


# future note - this is a better way to solve this task
# display_dict={str(index +1):meal for index, meal in enumerate(recipes)}
def add_to_shopping_dict(data: dict, item: str, amount: int):
    """Adds the missing amount of items to the shopping list"""
    if item in data:
        data[item] += amount
    else:
        data[item] = amount


display_dict = {}

shopping_list = []
shopping_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key
while True:
    # display a menu of the recipes how to cook
    print("Please choose your recipe")
    print(10 * "*")
    for key, value in display_dict.items():
        print(f"{key}: {value}")
    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients")
        ingredients = recipes[selected_item]
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t {food_item} - OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\t You need to buy {quantity_to_buy} of {food_item}")
                shopping_list.append({quantity_to_buy, food_item})
                add_to_shopping_dict(shopping_dict, food_item, quantity_to_buy)

        print(shopping_list)
        print(shopping_dict)

for thing in shopping_dict.items():
    print(thing)
