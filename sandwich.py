from enum import Enum, StrEnum


class SandwichPrice(Enum):
    CHICKEN: float = 5.25
    BEEF: float = 6.25
    TOFU: float = 5.75


class SandwichType(StrEnum):
    CHICKEN = "Chicken"
    BEEF = "Beef"
    TOFU = "Tofu"
    NOT_CHOSEN_YET = "Not yet chosen"
