
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
is_on=True

while is_on:
    options=menu.get_items()
    choice=input(f"What would you like ({options}):")
    if choice=='off':
        is_on=False
    elif choice=='report':
        coffee_maker.report()#print current amount of ingredients in machine
        money_machine.report()#print current amount of money in machine
    else:
        drink=menu.find_drink(choice)
        #drink is  menu object and cost is it attribute
        if coffee_maker.is_resource_sufficient(drink):
            if  money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

