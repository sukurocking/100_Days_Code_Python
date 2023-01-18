MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Print report, tell the user about the amount of available resources - coffee, milk, water
def print_report(resources_dict):
    for ingred, available_amount in resources_dict.items():
        print(f"{ingred} : {available_amount}")

def resource_check(coffee_type_dict, resources_dict):  # Needs to be modified
    dict_ingredients = MENU[coffee_type_dict]['ingredients']
    missing = ''
    for ingredient in dict_ingredients:
        if resources_dict[ingredient] < dict_ingredients[ingredient]:
            missing = missing + ' ' + ingredient
    if missing != '':
        print(f"Not enough resources for the following ingredients: \n {missing}")
        return False
    else:
        return True

# TODO: 4. Ask user to insert coins. If not sufficient, tell the user its not sufficient.
def is_coin_sufficient(coffee_type, coin_sum):
    """Checks if the sum of the coins put in by user is sufficient or not"""
    if MENU[coffee_type]['cost'] > coin_sum:
        return False
    else:
        return True


# TODO: 2. Ask the user what would he like? espresso, latte, cappuccino
continue_coffee_machine = True
while continue_coffee_machine:
    coffee_choice = input("What would you like to have? espresso, latte, cappuccino : ").lower()
    if coffee_choice == 'off':
        continue_coffee_machine = False
    elif coffee_choice == 'report':
        print_report(resources)  # Prints report for available resources
    else:
        # TODO: 3. Check against the availability of resources if they are available for the type of coffee,
        if not resource_check(coffee_choice, resources):
            pass
        # TODO: 4. Ask user to insert coins. If not sufficient, tell the user its not sufficient. If sufficient,
        #  go ahead give the coffee and deduct from resources
        else:
            print("Please insert coins")
            total_coin_sum = int(input("How many quarters?: ")) * 0.25
            total_coin_sum += int(input("How many nickels?: ")) * 0.10
            total_coin_sum += int(input("How many dimes?: ")) * 0.05
            total_coin_sum += int(input("How many pennies?: ")) * 0.01

            if not is_coin_sufficient(coffee_choice, total_coin_sum):
                print("Sorry that's not enough money. Money refunded")
            else:
                print(f"Here is your {coffee_choice}. Enjoy!")
                # Deduct from resources:
                for key,value in MENU[coffee_choice]['ingredients'].items():
                    resources[key] -= value
                refund_amount = total_coin_sum - MENU[coffee_choice]['cost']
                print(f"Here is your change ${refund_amount}")

# print_report(resources)


