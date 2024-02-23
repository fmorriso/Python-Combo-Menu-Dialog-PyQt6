from typing import ClassVar


class Order():

    KETCHUP_PACKET_COST : ClassVar[float] = 0.25
    def __init__(self):
        self.total_price : float = 0
        self.sandwich_type: str = ''
        self.sandwich_cost: float = 0
        self.beverage_type: str = ''
        self.beverage_cost: float = 0
        self.fries_size: str = ''
        self.fries_cost: float = 0
        self.ketchup_packets: int = 0
        self.ketchup_cost: float = 0

    def __str__(self):
        return f'Order Total: ${self.total_price}\n\tSandwich: {self.sandwich_type} ${self.sandwich_cost}'