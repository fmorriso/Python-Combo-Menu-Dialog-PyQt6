# Project 3.1.3 - Combo Menu - Simple
# Author: Fred Morrison

import sys

from beverage import *
from order import Order
from sandwich import *


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def start_new_order() -> Order:
    new_order = Order()
    return new_order


def get_sandwich(current_order: Order) -> None:
    while current_order.sandwich_type == SandwichType.NOT_CHOSEN_YET:
        prompt: str = 'Which sandwich would you like to order ('
        for en in SandwichType:
            prompt += f'{en.value}, '
        prompt = prompt.replace(f', {SandwichType.NOT_CHOSEN_YET.value}, ', '')
        prompt = prompt.removesuffix(', ') + ')?>'

        choice = input(prompt).lower().strip()
        match choice[:1]:

            case 'c':
                current_order.sandwich_type = SandwichType.CHICKEN
                current_order.sandwich_cost = SandwichPrice.CHICKEN.value

            case 'b':
                current_order.sandwich_type = SandwichType.BEEF
                current_order.sandwich_cost = SandwichPrice.BEEF.value

            case 't':
                current_order.sandwich_type = SandwichType.TOFU
                current_order.sandwich_cost = SandwichPrice.TOFU.value

            case other:
                print(f'{choice} is not valid. Please try again.')

    current_order.total_price = current_order.total_price + current_order.sandwich_cost


def get_beverage(current_order: Order) -> None:
    while current_order.beverage_size == BeverageSize.NOT_CHOSEN_YET:
        yesno = input('Do you want a beverage (y/n)?>').strip().lower()
        if yesno[:1] != 'y':
            current_order.beverage_size = BeverageSize.NONE
            return

        prompt = 'What size beverage would you like to order ('
        for size in BeverageSize:
            prompt += f'{size.value}, '

        prompt = prompt.replace(f', {BeverageSize.NOT_CHOSEN_YET.value}, ', '')
        prompt = prompt.replace(f', {BeverageSize.NONE.value}', '')
        prompt = prompt.removesuffix(', ') + ')?>'

        choice = input(prompt).lower().strip()
        match choice[:1]:

            case 's':
                current_order.beverage_size = BeverageSize.SMALL
                current_order.beverage_cost = BeveragePrice.SMALL.value

            case 'm':
                current_order.beverage_size = BeverageSize.MEDIUM
                current_order.beverage_cost = BeveragePrice.MEDIUM.value

            case 'l':
                current_order.beverage_size = BeverageSize.LARGE
                current_order.beverage_cost = BeveragePrice.LARGE.value

            case other:
                print(f'{choice} is not valid. Please try again.')

        current_order.total_price += current_order.beverage_cost


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    order: Order = start_new_order()

    get_sandwich(order)
    print(f'After ordering a sandwich\n{order}')

    get_beverage(order)
    print(f'After beverage selection\n{order}')
