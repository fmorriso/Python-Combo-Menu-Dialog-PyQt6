# Project 3.1.3 - Combo Menu - Simple using PyQT for dialogs
# Author: Fred Morrison

import sys
from enum import StrEnum

import beverage
import fries
import input_utilities
from order import Order
import sandwich


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def start_new_order() -> Order:
    new_order = Order()
    return new_order


def get_sandwich() -> None:
    # sandwich is mandatory, so trap user in a loop
    # until they make a proper sandwich choice.
    title: str = "Sandwich Choice"
    prompt: str = "Which sandwich would you like to order?"
    choices: list[str] = []
    types: list[str] = []
    prices: list[str] = []
    for type in sandwich.SandwichType:
        types.append(type.value)
    for price in sandwich.SandwichPrice:
        prices.append(f'${price.value:.2f}')
    for i in range(len(types)):
        choices.append(f'{types[i]} {prices[i]}')

    choice = input_utilities.InputUtils.get_single_choice(title, prompt, choices)
    choice = choice.lower()[0]
    # print(f'choice={choice}')
    match choice:

        case 'c':
            order.sandwich_type = sandwich.SandwichType.CHICKEN
            order.sandwich_cost = sandwich.SandwichPrice.CHICKEN.value

        case 'b':
            order.sandwich_type = sandwich.SandwichType.BEEF
            order.sandwich_cost = sandwich.SandwichPrice.BEEF.value

        case 't':
            order.sandwich_type = sandwich.SandwichType.TOFU
            order.sandwich_cost = sandwich.SandwichPrice.TOFU.value

        case _:
            print(f'{choice} is not valid. Please try again.')

    order.total_price = order.total_price + order.sandwich_cost


def get_beverage() -> None:
    yesno = input_utilities.InputUtils.get_yesno_response("Do you want a beverage?", "Beverage")
    if not yesno:
        order.beverage_size = None
        return

    title: str = 'Beverage Choice'
    prompt: str = 'What size beverage would you like to order?'
    choices: list[str] = []
    sizes: list[StrEnum] = []
    prices: list[str] = []
    for size in beverage.BeverageSize:
        sizes.append(size.value)
    for price in beverage.BeveragePrice:
        prices.append(f'${price.value:.2f}')
    for i in range(len(sizes)):
        choices.append(f'{sizes[i]} {prices[i]}')

    # choice = input(prompt).lower().strip()
    choice = input_utilities.InputUtils.get_single_choice(title, prompt, choices)
    choice = choice.lower()[0]
    match choice:

        case 's':
            order.beverage_size = beverage.BeverageSize.SMALL
            order.beverage_cost = beverage.BeveragePrice.SMALL.value

        case 'm':
            order.beverage_size = beverage.BeverageSize.MEDIUM
            order.beverage_cost = beverage.BeveragePrice.MEDIUM.value

        case 'l':
            order.beverage_size = beverage.BeverageSize.LARGE
            order.beverage_cost = beverage.BeveragePrice.LARGE.value

        case _:
            print(f'{choice} is not valid. Please try again.')

    order.total_price += order.beverage_cost


def get_fries() -> None:
    yesno = input_utilities.InputUtils.get_yesno_response('Do you want fries?', 'French Fries')
    if not yesno:
        order.fries_size = None
        return

    title: str = 'Fries Choice'
    prompt = 'What size fries would you like to order?'
    choices: list[str] = []
    sizes: list[str] = []
    prices: list[str] = []
    for size in fries.FriesSize:
        sizes.append(size.value)
    for price in fries.FriesPrice:
        prices.append(f'${price.value:.2f}')
    for i in range(len(sizes)):
        choices.append(f'{sizes[i]} {prices[i]}')

    choice = input_utilities.InputUtils.get_single_choice(title, prompt, choices)
    choice = choice.lower()[0]
    match choice:

        case 's':
            order.fries_size = fries.FriesSize.SMALL
            order.fries_cost = fries.FriesPrice.SMALL.value
            yesno = input_utilities.InputUtils.get_yesno_response('Do you want to super-size to Large fries?', 'Super-size')
            if yesno:
                order.fries_size = fries.FriesSize.LARGE
                order.fries_cost = fries.FriesPrice.LARGE.value

        case 'm':
            order.fries_size = fries.FriesSize.MEDIUM
            order.fries_cost = fries.FriesPrice.MEDIUM.value

        case 'l':
            order.fries_size = fries.FriesSize.LARGE
            order.fries_cost = fries.FriesPrice.LARGE.value

        case other:
            print(f'{choice} is not valid. Please try again.')

    order.total_price += order.fries_cost


def get_ketchup_packets() -> None:
    yesno = input_utilities.InputUtils.get_yesno_response("Do you want any ketchup packets?", "Ketchup Packets")
    if not yesno:
        return

    n: int = input_utilities.InputUtils.get_whole_number('How many ketchup packets?', 'Ketchup Packets')

    order.ketchup_packets = n
    order.ketchup_cost = order.ketchup_packets * order.KETCHUP_PACKET_COST

    order.total_price += order.ketchup_cost


def check_for_discount():
    if order.sandwich_cost > 0 and order.beverage_cost > 0 and order.fries_cost > 0:
        order.total_price -= 1
        order.discount_applied = True


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    order: Order = start_new_order()

    get_sandwich()
    # print(f'After ordering a sandwich\n{order}')

    get_beverage()
    # print(f'After beverage selection\n{order}')n

    get_fries()
    # print(f'After fries selection\n{order}')

    get_ketchup_packets()

    check_for_discount()

    print(f'Your order:\n{order}')
