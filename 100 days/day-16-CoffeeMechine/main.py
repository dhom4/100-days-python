from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

""" Notes:
 1. Create an object from the class MoneyMachine(), than only you can use it
 2. Name convention is the object sneak_case, and the Object PascalCase like: 
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
 3. it make the main code shorter
"""

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_off = False
while not is_off:
    options = menu.get_items()
    user_order = input(f"What would you like ({options}) :").lower()
    if user_order == "off":
        off = True
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
