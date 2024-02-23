# Project 3.1.3 - Combo Menu - Simple
# Author: Fred Morrison

import sys
from order import Order
from sandwich import *


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def start_new_order() -> Order:
    order = Order()
    return order


def get_sandwich(order: Order) -> None:
    while order.sandwich_type == '':
        prompt: str = 'Which sandwich would you like to order ('
        for en in SandwichType:
            prompt += f'{en}, '
        prompt = prompt.removesuffix(', ') + ')?>'

        choice = input(prompt).lower().strip()
        match choice[:1]:

            case 'c':
                order.sandwich_type = SandwichType.CHICKEN
                order.sandwich_price = SandwichPrice.CHICKEN

            case 'b':
                order.sandwich_type = SandwichType.BEEF
                order.sandwich_price = SandwichPrice.BEEF

            case 't':
                order.sandwich_type = SandwichType.TOFU
                order.sandwich_price = SandwichPrice.TOFU

            case other:
                print(f'{choice} is not valid. Please try again.')

    order.total_price = order.total_price + order.sandwich_price.value


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    order: Order = start_new_order()
    get_sandwich(order)
    print(f'After ordering a sandwich\n{order}')
