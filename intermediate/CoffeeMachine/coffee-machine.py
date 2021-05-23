from arts_resources import MENU, resources

profit = 0
off_machine = False

print('This is just for testing')


# check resource sufficient
def check_resource_sufficient(order_ingredient):
    """Return true if the ingredient is sufficient else false"""
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


# process the coin
def process_coin():
    """Returns the total calculated form the inserted coin"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# is transaction successful
def is_transaction_successful(money_received, drink_cost):
    """Return ture if transaction is successful else False"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False


# make coffee
def make_coffee(drink_name, order_ingredient):
    """Deduct the require ingredient from the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here, is your {drink_name}. Enjoy!")


while not off_machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        off_machine = True

    elif choice == "report":
        print(f"Water: {resources['water']}ml \n"
              f"Milk: {resources['milk']}ml \n"
              f"Coffee: {resources['coffee']}g \n"
              f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

