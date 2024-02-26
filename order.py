from typing import ClassVar

from beverage import BeverageSize
from fries import FriesSize
from sandwich import SandwichType


class Order():
    KETCHUP_PACKET_COST: ClassVar[float] = 0.25

    def __init__(self):
        self.total_price: float = 0.0
        self.sandwich_type: SandwichType = SandwichType.NOT_CHOSEN_YET
        self.sandwich_cost: float = 0.0
        self.beverage_size: BeverageSize = BeverageSize.NOT_CHOSEN_YET
        self.beverage_cost: float = 0.0
        self.fries_size: FriesSize = FriesSize.NOT_CHOSEN_YET
        self.fries_cost: float = 0.0
        self.ketchup_packets: int = 0
        self.ketchup_cost: float = 0.0

    def __str__(self):
        retval: str = f'Order Total: ${self.total_price:.2f}'

        # add sandwich information if one has been chosen
        if self.sandwich_type != SandwichType.NOT_CHOSEN_YET:
            retval += f'\n\tSandwich: {self.sandwich_type.value} ${self.sandwich_cost:.2f}'

        # add beverage information if available
        if self.beverage_size != BeverageSize.NOT_CHOSEN_YET:
            retval += f'\n\tBeverage: '
            if self.beverage_size == BeverageSize.NONE:
                retval += 'None'
            else:
                retval += f'{self.beverage_size.value} ${self.beverage_cost:.2f}'

        # fires information if available
        if self.fries_size != FriesSize.NOT_CHOSEN_YET:
            retval += f'\n\tFries: '
            if self.fries_size == FriesSize.NONE:
                retval += 'None'
            else:
                retval += f'{self.fries_size.value} ${self.fries_cost:.2f}'

        return retval
