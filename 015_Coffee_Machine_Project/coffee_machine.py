def menu(menu_list):
    print("Welcome to the coffee machine!\n")
    print("Select which coffee you would like:")
    for i in range(len(menu_list)):
        print(f"\t{i + 1} \t {list(menu_list)[i].capitalize()} \t ${menu_list[list(menu_list)[i]]['price']:.2f}")

    while True:
        drink = input("\t>>  ").casefold()

        if drink in menu_list.keys():
            print(f"\nChecking if {drink} can be made...")
            return drink
        elif drink == "off" or drink == "report":
            print("\nPreparing for maintenance")
            return drink
        else:
            print("\nInvalid choice. Please try again.")


def resource_check(resource_list, menu_list, chosen_drink):
    ingredients = dict(menu_list[chosen_drink]["ingredients"])

    if ingredients["water"] > resource_list["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif ingredients["coffee"] > resource_list["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    elif "milk" in ingredients and ingredients["milk"] > resource_list["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    else:
        return True


def take_payment(coin_values):
    total_paid = 0

    for key, value in coin_values.items():
        while True:
            try:
                amount = int(input(f"Enter number of {key}: "))
                total_paid += amount * value
                break
            except ValueError:
                print("Please enter a valid amount")

    return total_paid


def give_change(drink_price, payment_made):
    amount_due = payment_made - drink_price
    return amount_due


def make_coffee(coffee_choice, menu_list, resources_list):
    ingredients = dict(menu_list[coffee_choice]["ingredients"])

    for key, value in ingredients.items():
        resources_list[key] -= value

    print(f"\nHere is your {coffee_choice}. Enjoy!\n")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "price": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "price": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "price": 3
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

if __name__ == "__main__":
    while True:
        drink_choice = menu(MENU)
        if drink_choice != "off" and drink_choice != "report":
            drink_possibility = resource_check(resources, MENU, drink_choice)
            if drink_possibility:
                price = MENU[drink_choice]["price"]
                print(f"{drink_choice.capitalize()} can be made")
                print(f"Price: \t ${price:.2f}\n")

                amount_paid = take_payment(COINS)
                change = give_change(price, amount_paid)
                make_coffee(drink_choice, MENU, resources)
                print(f"Your change is ${change:.2f}\n")
            else:
                print("Please call a maintenance worker")
        elif drink_choice == "report":
            for key, value in resources.items():
                print(f"{key} \t {value}")
            break
        else:
            break