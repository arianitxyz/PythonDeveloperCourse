from contents import pantry, recipes

# future note - this is a better way to solve this task
# display_dict={str(index +1):meal for index, meal in enumerate(recipes)}

display_dict = {}
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
        for food_item in ingredients:
            if food_item in pantry:
                print(f"\t {food_item} - OK")
            else:
                print(f"\t {food_item} - missing")
        print(ingredients)
