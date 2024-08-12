import sys
import drink_menu

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def user_menu():
    while True:
        print(" ------------------------------------")
        print("|                                    |")
        print("|          COFFEE MACHINE            |")
        print("|                                    |")
        print(" ------------------------------------")
        print("What would you like?")
        print("1: Espresso")
        print("2: Latte")
        print("3: Cappuccino")
        selection = input("] ")
        match selection:
            case '1':
                return 'espresso'
            case '2':
                return 'latte'
            case '3':
                return 'cappuccino'
            case 'report':
                return 'report'
            case 'off':
                sys.exit(0)
            case _:
                print("Invalid option, please try again.")


def print_report():
    print(f"Water:\t{resources["water"]}ml")
    print(f"Milk:\t{resources["milk"]}ml")
    print(f"Coffee:\t{resources["coffee"]}g")
    print(f"Money:\t${resources["money"]:.2f}")


def check_resources(selected_drink):
    has_sufficient_resources = True
    resources_lacking = []
    ingredients = drink_menu.MENU[selected_drink]["ingredients"]
    for ingredient in ingredients:
        if drink_menu.MENU[selected_drink]["ingredients"][ingredient] > resources[ingredient]:
            has_sufficient_resources = False
            resources_lacking.append(ingredient)
    if not has_sufficient_resources:
        print(f"Sorry, there is not enough {", ".join(resources_lacking)}")
    return has_sufficient_resources


def take_payment(selected_drink):
    price = drink_menu.MENU[selected_drink]['cost']
    amount_paid = 0
    done_entering_coins = False
    while amount_paid < price and not done_entering_coins:
        print(f"The amount due is ${price - amount_paid:.2f}")
        print("Enter coins:")
        print("Q) quarter")
        print("D) dime")
        print("N) nickel")
        print("P) penny")
        print("X) done entering coins")
        entered_coin = input("] ").upper()
        match entered_coin:
            case 'Q':
                amount_paid += .25
            case 'D':
                amount_paid += .1
            case 'N':
                amount_paid += .05
            case 'P':
                amount_paid += .01
            case 'X':
                done_entering_coins = True
            case _:
                "Please enter the correct value."
    if amount_paid < price:
        print(f"Sorry, you are ${price - amount_paid:.2f} short")
        return False
    elif amount_paid > price:
        print(f"Here is your change: ${amount_paid - price:.2f}")
    else:
        print("You entered the exact amount. Thank you")
    resources['money'] += price
    return True


def make_drink(selected_drink):
    ingredients = drink_menu.MENU[selected_drink]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= drink_menu.MENU[selected_drink]["ingredients"][ingredient]
    return True


# coffee machine main
while True:
    selection = user_menu()
    print("")
    match selection:
        case 'report':
            print_report()
        case 'espresso' | 'latte' | 'cappuccino':
            if check_resources(selection):
                if take_payment(selection):
                    print("Making Drink")
                    if make_drink(selection):
                        print(f"Here is your {selection}. Enjoy!")
        case _:
            print("Unknown error")
    print("")
