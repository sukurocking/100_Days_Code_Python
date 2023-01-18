from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mymenu = Menu()
mycoffeemaker = CoffeeMaker()
mymoneymachine = MoneyMachine()
# print(mymenu.get_items())

coffee_machine_is_on = True
while coffee_machine_is_on:
    user_input = input(f"What would you like to have? {mymenu.get_items()} ")
    if user_input == 'off':
        coffee_machine_is_on = False
    elif user_input == 'report':
        mycoffeemaker.report()
        mymoneymachine.report()
    else:
        drink = mymenu.find_drink(user_input)
        if mycoffeemaker.is_resource_sufficient(drink):
            if mymoneymachine.make_payment(drink.cost):
                mycoffeemaker.make_coffee(drink)