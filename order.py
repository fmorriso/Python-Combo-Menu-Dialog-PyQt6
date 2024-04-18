from typing import ClassVar

from beverage import BeverageSize
from fries import FriesSize
from sandwich import SandwichType


class Order:
    KETCHUP_PACKET_COST: ClassVar[float] = 0.25

    def __init__(self):
        self.total_price: float = 0.0
        self.sandwich_type: SandwichType = None
        self.sandwich_cost: float = 0.0
        self.beverage_size: BeverageSize = None
        self.beverage_cost: float = 0.0
        self.fries_size: FriesSize = None
        self.fries_cost: float = 0.0
        self.ketchup_packets: int = 0
        self.ketchup_cost: float = 0.0
        self.discount_applied: bool = False

    def __str__(self):
        """Print a human-readable representation of the Order"""
        retval: str = f'Order Total: ${self.total_price:.2f}'

        # add sandwich information if one has been chosen
        if self.sandwich_type is not None:
            retval += f'\n\tSandwich: {self.sandwich_type.value} ${self.sandwich_cost:.2f}'

        # add beverage information if available
        # if self.beverage_size is not None:
        retval += f'\n\tBeverage: '
        if self.beverage_size is None:
            retval += 'None'
        else:
            retval += f'{self.beverage_size.value} ${self.beverage_cost:.2f}'

        # fires information if available
        retval += f'\n\tFries: '
        if self.fries_size is None:
            retval += 'None'
        else:
            retval += f'{self.fries_size.value} ${self.fries_cost:.2f}'

        # ketchup packets
        if self.ketchup_packets == 0:
            retval += '\n\tKetchup packets: None'
        else:
            retval += f'\n\tKetchup packets: {self.ketchup_packets}  ${self.ketchup_cost:.2f}'

        # show discount was applied if applicable
        if self.discount_applied:
            retval += '\n\t*** $1 discount applied ***'

        return retval
