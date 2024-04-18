# these are the french fries sizes and prices using symbols instead
# of "magic numbers" and "magic strings"
from enum import Enum


class FriesSize(Enum):
    SMALL: str = 'Small'
    MEDIUM: str = 'Medium'
    LARGE: str = 'Large'


class FriesPrice(Enum):
    SMALL: float = 1.00
    MEDIUM: float = 1.50
    LARGE: float = 2.0
