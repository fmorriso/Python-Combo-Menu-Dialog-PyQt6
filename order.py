from typing import ClassVar

from sandwich import SandwichType


class Order():
    KETCHUP_PACKET_COST: ClassVar[float] = 0.25

    def __init__(self):
        self.total_price: float = 0.0
        self.sandwich_type: SandwichType = SandwichType.NOT_CHOSEN_YET
        self.sandwich_cost: float = 0.0
        self.beverage_size: str = ''  # TODO: change to BeverageSize
        self.beverage_cost: float = 0.0
        self.fries_size: str = ''  # TODO: change to FriesSize
        self.fries_cost: float = 0.0
        self.ketchup_packets: int = 0
        self.ketchup_cost: float = 0.0

    def __str__(self):
        retval: str = f'Order Total: ${self.total_price:.2f}'

        # add sandwich information if one has been chosen
        if self.sandwich_type != SandwichType.NOT_CHOSEN_YET:
            retval += f'\n\tSandwich: {self.sandwich_type.value} ${self.sandwich_cost:.2f}'

        return retval
