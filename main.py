from data import MENU, resources


Money=0
is_on=True


def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item] :
            print(f"Sorry not sufficient {item} left for your order.")
            return False

    return True


def process_coins():
    """Return the total calculated of the inputed coin"""
    print("Please insert coins")
    quaters = int(input("How many quaters : ")) * 0.25
    dimes = int(input("How many Dimes : ")) * 0.10
    nickel = int(input("How many nickels : ")) * 0.05
    penny = int(input("How many penny : ")) * 0.01
    total=quaters+dimes+nickel+penny
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global Money
        Money+= drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name,orderingredients) :
    for item in orderingredients :
        resources[item] -= orderingredients[item]
    print(f"Here is your {drink_name}, Enjoy ☕")


while is_on :
    type_of_coffee = input("Which type of coffee would you like 'espresso'/'latte'/cappuccino : \n").lower()

    if type_of_coffee == "off":
        is_on = False
    elif type_of_coffee == "report" :
        print(f"Water:{resources['water']}")
        print(f"Milk: {resources['milk']}" )
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {Money}")
    else :
        drink=MENU[type_of_coffee]
        if is_resource_sufficient(drink["ingredients"]) :
            payment=process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(type_of_coffee, drink["ingredients"])









