import os
from time import sleep
from dictionary import MENU

should_continue = True
money = 0
resources = {
    "water":300,
    "milk": 200,
    "coffee": 100
}


def turn_off():
    print("This screen will clear out in a moment.")
    sleep(1)
    os.system('cls')
    quit()


def report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink_ingredients):
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
        else:
            return True


def count_coins():
    quarters = float(input("Quarters: $"))* 0.25
    dimes = float(input("Dimes : $"))* 0.1
    nickles = float(input("Nickles : $"))* 0.05
    pennies = float(input("Pennies : $"))* 0.01
    amount = quarters + dimes + nickles + pennies
    return amount


def refund(paid, price):
    global money
    change = paid - price
    money += price
    print(f"Here's your change ${change}.")


def successful_transaction(paid, drinks_cost):
    global money
    if paid == drinks_cost:
        money += paid
        return True
    if paid > drinks_cost:
        refund(paid, drinks_cost)
        return True
    if paid < drinks_cost:
        return False


def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}. Enjoy!")


while should_continue:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        turn_off()
    if order == "report":
        report()
    if order == "espresso" or order == "latte" or order == "cappuccino":
        drink = MENU[order]
        drink_cost = drink["cost"]
        drink_ingredients = drink["ingredients"]
        if check_resources(drink_ingredients):
            payment = count_coins()
            print(f"You gave me ${payment}")
            print(f"Your {order} will cost ${drink_cost}.")
            processing_order = successful_transaction(payment, drink_cost)
            if processing_order:
                make_drink(order, drink_ingredients)
            else:
                print("Sorry, money not enough")
        else:
            keep_ordering = input("Would you like to order something else or get a refund? Type 'else' or 'refund' ").lower()
            if keep_ordering == "else":
                should_continue = True
            if keep_ordering == "refund":
                refund(payment*2, payment)