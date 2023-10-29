from cgitb import reset
from menuAndInput import menu, resources

profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️ . Enjoy!")
    
    
def add_resources():
    """Add resources to the coffee machine."""
    print("Add resources to the coffee machine.")
    resources["water"] += int(input("How many ml of water do you want to add?: "))
    resources["milk"] += int(input("How many ml of milk do you want to add?: "))
    resources["coffee"] += int(input("How many grams of coffee do you want to add?: "))


def reset_profit():
    """Reset the profit to zero."""
    global profit
    profit = 0


while 1:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice.lower() in ['espresso', 'latte', 'cappuccino']:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "add":
        add_resources()
    elif choice == "reset":
        reset_profit()
    elif choice == "off":
        break
    else:
        print(f"check input")