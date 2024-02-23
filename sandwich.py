# these are the sandwich types and prices using symbols instead
# of "magic numbers" and "magic strings"
from enum import Enum


class SandwichPrice(Enum):
    CHICKEN: float = 5.25
    BEEF: float = 6.25
    TOFU: float = 5.75


class SandwichType(Enum):
    CHICKEN = "Chicken"
    BEEF = "Beef"
    TOFU = "Tofu"
    NOT_CHOSEN_YET = "Not yet chosen"
