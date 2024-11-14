favourite_foods = []

while True:
    print("\nFavourite Foods Manager")
    print("=======================")
    print("1. Add Food")
    print("2. Remove Food")
    print("3. View All Favourite Foods")
    print("0. Exit")

    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid choice! Please enter a number from 0 to 3.")
        continue

    if choice == 0:
        print("Thanks for using the Favourite Foods Manager. Goodbye!")
        break
    elif choice == 1:
        food = input("Enter your favourite food name: ").strip().capitalize()
        if food not in favourite_foods:
            favourite_foods.append(food)
            print(f"{food} has been added to your favourite foods list.")
        elif food in favourite_foods:
            print(f"{food} already exists in your favourite foods list.")
        else:
            print("Food name cannot be empty!")
    elif choice == 2:
        if not favourite_foods:
            print("Your favourite foods list is empty.")

        food = input("Enter the food you want to remove: ").strip().capitalize()
        if food in favourite_foods:
            favourite_foods.remove(food)
            print(f"{food} has been removed from your favourite foods list.")
        else:
            print(f"{food} is not in your favourite foods list.")
    elif choice == 3:
        if favourite_foods:
            print("--------------------------")
            print("Your favourite foods are:")
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}. {food}")
            print("--------------------------")
        else:
            print("Your favourite foods list is empty.")
    else:
        print("Invalid choice! Please enter a number from 0 to 3.")