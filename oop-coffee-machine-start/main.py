from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

game_over = False

money = MoneyMachine()
menu = Menu()
waiter = CoffeeMaker()

while not game_over:
    options = menu.get_items()
    user_input = (input(f"What would you like? ({options}): ")).lower()
    if user_input == "report":
        waiter.report()
        money.report()
    elif user_input == "off":
        game_over = True
    else:
        drink = menu.find_drink(user_input)
        print(drink.ingredients)
        if waiter.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                waiter.make_coffee(drink)