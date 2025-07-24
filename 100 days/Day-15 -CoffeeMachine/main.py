from so import drink

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
    "money" : 0
}

def print_report():
    print(f"Water:  {resources["water"]}mL\n"
          f"Milk:   {resources["milk"]}mL\n"
          f"Coffee: {resources["coffee"]}g\n"
          f"Money:  ${resources["money"]}\n")


def deduction(item):
    ings = MENU[item]["ingredients"]
    for ing in ings:
        resources[ing] -= ings[ing]

def is_enough(item):
    is_enough = True

    ings = MENU[item]["ingredients"]
    for ing in ings:
        if ings[ing] > resources[ing] :
            print(f"Sorry there is not enough {ing}")
            is_enough = False
    return is_enough


# TODO: 5. Process coins #  quarters = $0.25, #  dimes = $0.10, #  nickles = $0.05, #  pennies = $0.01
def process_coins():
    print("Please enter some conies: ")
    quarters = 0.25 * int(input())
    dimes = 0.10 * int(input())
    nickles = 0.05 * int(input())
    pennies = 0.01 * int(input())
    total = (quarters + dimes + nickles + pennies)
    return total

off = False
# TODO: 1. The prompt should show every time
while not off:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == "off":
        off = True
    # TODO: 3. Print report.
    elif user_input == "report":
        print_report()
    # TODO: 7. Make Coffee.
    else:




        # TODO: 6. Check transaction successful?
        total = process_coins()
        drink_price = MENU[user_input]["cost"]

        if total >= drink_price :

            # TODO: 4. Check resources sufficient?
            if is_enough(user_input):
                print("Here is your latte ☕️. Enjoy!\n\n")
                # TODO: deduct after making
                deduction(user_input)
                change = round(total - drink_price , 2)
                print(f"here is you change: ${change}\n\n")
            else:
                print("Sorry, not enough ingredients\n\n")

        else:
            print("Sorry not enough money")
            print(f"Total: ${total}\n\n")

# total = 2.4
# total = total // 0.25
# print(total)
# total = total // 0.1
# print(total)
