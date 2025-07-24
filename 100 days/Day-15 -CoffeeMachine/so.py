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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}


def main():
    is_on = True
    while is_on:
        choice = input("what would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            print_report()
        else:

            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffe(choice, drink["ingredients"])



def print_report():
    print(f"milk {resources["water"]}ml")
    print(f"coffee {resources["milk"]}ml")
    print(f"money {resources["coffee"]}g")
    print(f"Money ${profit}")

def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False when ingredient is insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough

def process_coins():
    """Return total calculated from the coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarter?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickel?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_receved, drink_cost):
    if money_receved >= drink_cost: # 0 check if money is enough to pressed
        change = round(money_receved - drink_cost, 2) # 1 return change
        print(f"Here is ${change} in change ")
        global profit # 2 increment profet
        profit += drink_cost

        return True
    else:
        print("Sorry not enough money, money refund")
        return False


def make_coffe(drink, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!\n")


main()