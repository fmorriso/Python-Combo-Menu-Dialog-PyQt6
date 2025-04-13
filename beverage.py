# these are the beverage sizes and prices using symbols instead
# of "magic numbers" and "magic strings"
from enum import Enum, StrEnum


class BeverageSize(StrEnum):
    SMALL: str = 'Small'
    MEDIUM: str = 'Medium'
    LARGE: str = 'Large'


class BeveragePrice(Enum):
    SMALL: float = 1.00
    MEDIUM: float = 1.50
    LARGE: float = 2.0
