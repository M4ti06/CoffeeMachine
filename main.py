from decimal import Decimal, getcontext

getcontext().prec = 3

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

money_collected = 0


def summing_the_money(which_money):
    """Adds the money inserted to the machine. Return the sum of all inserted coins"""
    sum_of_money_collected = 0
    for nominal, quantity in which_money.items():
        piece_of_sum = Decimal(nominal) * quantity
        sum_of_money_collected += piece_of_sum
    return sum_of_money_collected


def print_report():
    """Prints report about levels of resources left in the machine and amount of collected money"""
    print(f"Hello there! \nThis is the report of resources left in Yours machine:\n "
          f"Water: {resources['water']} ml\n Milk: {resources['milk']} ml\n Coffee: {resources['coffee']} grams \n "
          f"Money collected: {money_collected} Dollars")


def enough_money(which_coffee, money_collected):
    """Checks if the amount of money inserted to the machine is sufficient and process coins into machine.
    Returns multiple values. """
    inserted_money = {
        0.01: int(input("How many 0,01 coins do you want to put into machine?: ")),
        0.05: int(input("How many 0,05 coins do you want to put into machine?: ")),
        0.10: int(input("How many 0,10 coins do you want to put into machine?: ")),
        0.25: int(input("How many 0,25 coins do you want to put into machine?: ")),
    }
    sum_inserted_money = summing_the_money(inserted_money)
    cost = Decimal(MENU[which_coffee]["cost"])
    change = sum_inserted_money - cost
    if cost <= sum_inserted_money:
        money_collected += cost
        return True, change, money_collected
    else:
        return False, sum_inserted_money, money_collected


def is_enough_resources(which_coffee):
    """Checks if the resources available in the machine is sufficient to make a coffee"""
    if which_coffee != "espresso":
        if MENU[which_coffee]["ingredients"]["water"] <= resources["water"] and \
                MENU[which_coffee]["ingredients"]["milk"] <= resources["milk"] and \
                MENU[which_coffee]["ingredients"]["coffee"] <= resources["coffee"]:
            return True
        else:
            return False
    else:
        if MENU[which_coffee]["ingredients"]["water"] <= resources["water"] and \
                MENU[which_coffee]["ingredients"]["coffee"] <= resources["coffee"]:
            return True
        else:
            return False


def brewing_coffe(which_coffee, money_collected):
    """Logic about making a coffee."""
    needed_water = MENU[which_coffee]["ingredients"]["water"]
    if which_coffee != "espresso":
        needed_milk = MENU[which_coffee]["ingredients"]["milk"]
    needed_coffee = MENU[which_coffee]["ingredients"]["coffee"]
    is_enough_money, change_to_give, money_collected_overall = enough_money(choose_the_coffee, money_collected)
    if is_enough_money and is_enough_resources(which_coffee):
        resources["water"] -= needed_water
        if which_coffee != "espresso":
            resources["milk"] -= needed_milk
        resources["coffee"] -= needed_coffee
        print(f"Be happy with your delicious{which_coffee}!")
        print(f"You have {change_to_give} Dollars change")
        return money_collected_overall
    elif not is_enough_resources(which_coffee):
        print("You dont have enough resources, plz refill")
    else:
        print(f"Sorry You dont have enough money.")
        print(f"You have {change_to_give + Decimal(MENU[which_coffee]['cost'])} Dollars change")


still_making_coffee = True
while still_making_coffee:
    choose_the_coffee = input("Choose the coffee You like: espresso, latte, cappuccino: ")
    if choose_the_coffee != "report":
        if not is_enough_resources(choose_the_coffee):
            print("Unfortunatelly we dont have enough resources for Your coffee.")
    if choose_the_coffee == "report":
        print_report()
    else:
        money_collected = brewing_coffe(choose_the_coffee, money_collected)

    another_coffee = input("Do You want a cup of coffee? Type 'y' or 'n': ")
    if another_coffee == "n":
        still_making_coffee = False
