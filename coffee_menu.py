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

profit = 0
is_on = True


def resources_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry! Not enough {item} available!")
            return False
    return True


def calculate_coins():
    print("Please insert coins.\n")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, cost_of_drink, drink):
    if money_received > cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Cost of a {drink} is ${cost_of_drink}. Money received was ${money_received}.")
        print(f"Here is ${change} in change\n")
        global profit
        profit += cost_of_drink
        return True
    else:
        print(f"Sorry, cost of a {drink} is ${cost_of_drink}. Money received was ${money_received}.")
        print("Not enough money. Money refunded\n")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️\n")


while is_on:
    choice = ""
    choice = input("What kind of coffee would you like? (Espresso/Latte/Cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}mL ")
        print(f"Milk: {resources['milk']}mL ")
        print(f"Coffee: {resources['coffee']}g ")
        print(f"Money: ${profit} ")
    else:
        drink = MENU[choice]
        if resources_enough(drink["ingredients"]):
            payment = calculate_coins()
            if is_transaction_successful(payment, drink["cost"], choice):
                make_coffee(choice, drink["ingredients"])

print("Have a great day! :)")
