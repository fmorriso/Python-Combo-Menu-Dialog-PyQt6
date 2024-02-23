# Project 3.1.3 - Combo Menu - Simple
# Author: Fred Morrison

import sys
from order import Order
from sandwich import *


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def start_new_order() -> Order:
    new_order = Order()
    return new_order


def get_sandwich(order: Order) -> None:
    while order.sandwich_type == SandwichType.NOT_CHOSEN_YET:
        prompt: str = 'Which sandwich would you like to order ('
        for en in SandwichType:
            prompt += f'{en.value}, '
        prompt = prompt.replace(f', {SandwichType.NOT_CHOSEN_YET.value}, ', '')
        prompt = prompt.removesuffix(', ') + ')?>'

        choice = input(prompt).lower().strip()
        match choice[:1]:

            case 'c':
                order.sandwich_type = SandwichType.CHICKEN
                order.sandwich_cost = SandwichPrice.CHICKEN.value

            case 'b':
                order.sandwich_type = SandwichType.BEEF
                order.sandwich_cost = SandwichPrice.BEEF.value

            case 't':
                order.sandwich_type = SandwichType.TOFU
                order.sandwich_cost = SandwichPrice.TOFU.value

            case other:
                print(f'{choice} is not valid. Please try again.')

    order.total_price = order.total_price + order.sandwich_cost


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    order: Order = start_new_order()
    get_sandwich(order)
    print(f'After ordering a sandwich\n{order}')

