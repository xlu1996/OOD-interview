from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass


# ======= Enums =======
class Topping(Enum):
    CHEESE = "cheese"
    PEPPERONI = "pepperoni"
    OLIVES = "olives"
    BACON = "bacon"
    MUSHROOM = "mushroom"
    ONION = "onion"


class Size(Enum):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"


# ======= Price Configs =======
TOPPING_PRICES: dict[Topping, float] = {
    Topping.CHEESE: 2.0,
    Topping.PEPPERONI: 3.0,
    Topping.OLIVES: 1.5,
    Topping.BACON: 2.5,
    Topping.MUSHROOM: 1.0,
    Topping.ONION: 0.5,
}

PIZZA_BASE_PRICE: dict[Size, float] = {
    Size.SMALL: 6.0,
    Size.MEDIUM: 8.0,
    Size.LARGE: 10.0,
}

FRIES_PRICES: dict[Size, float] = {
    Size.SMALL: 2.0,
    Size.MEDIUM: 3.0,
    Size.LARGE: 4.0,
}


# ======= Abstract Item =======
class Item(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


# ======= Set Pizza (predefined) =======
@dataclass
class SetPizza(Item):
    name: str
    price: float

    def get_description(self) -> str:
        return f"Set Pizza: {self.name}"

    def get_cost(self) -> float:
        return self.price


# ======= Custom Pizza (with toppings list) =======
@dataclass
class CustomPizza(Item):
    size: Size
    toppings: list[Topping]

    def get_description(self) -> str:
        topping_names = ", ".join(t.value.capitalize() for t in self.toppings)
        return f"Custom Pizza ({self.size.value}): {topping_names or 'Plain'}"

    def get_cost(self) -> float:
        base = PIZZA_BASE_PRICE[self.size]
        topping_cost = sum(TOPPING_PRICES[t] for t in self.toppings)
        return base + topping_cost


# ======= Other Items =======
@dataclass
class Fries(Item):
    size: Size

    def get_description(self) -> str:
        return f"Fries ({self.size.value})"

    def get_cost(self) -> float:
        return FRIES_PRICES[self.size]


@dataclass
class Cookie(Item):
    quantity: int = 1
    unit_price: float = 1.5

    def get_description(self) -> str:
        return f"Cookie x{self.quantity}"

    def get_cost(self) -> float:
        return self.quantity * self.unit_price


@dataclass
class Drink(Item):
    name: str
    price: float

    def get_description(self) -> str:
        return f"Drink: {self.name}"

    def get_cost(self) -> float:
        return self.price


# ======= Order =======
class Order:
    def __init__(self):
        self.items: list[Item] = []

    def add(self, item: Item) -> "Order":
        self.items.append(item)
        return self  # allow chaining

    def get_total(self) -> float:
        return sum(item.get_cost() for item in self.items)

    def show(self):
        print("=" * 40)
        print("ORDER SUMMARY")
        print("=" * 40)
        for item in self.items:
            print(f"  {item.get_description():<30} ${item.get_cost():>6.2f}")
        print("-" * 40)
        print(f"  {'TOTAL':<30} ${self.get_total():>6.2f}")
        print("=" * 40)


# ======= Demo =======
if __name__ == "__main__":
    order = Order()

    # 1. Set Pizza
    order.add(SetPizza(name="Margherita Special", price=12.0))

    # 2. Custom Pizza with toppings
    order.add(CustomPizza(
        size=Size.LARGE,
        toppings=[Topping.CHEESE, Topping.PEPPERONI, Topping.BACON]
    ))

    # 3. Another custom pizza (plain)
    order.add(CustomPizza(
        size=Size.SMALL,
        toppings=[]
    ))

    # 4. Sides
    order.add(Fries(size=Size.LARGE))
    order.add(Fries(size=Size.SMALL))

    # 5. Cookies
    order.add(Cookie(quantity=3))

    # 6. Drinks
    order.add(Drink(name="Coke", price=2.5))
    order.add(Drink(name="Orange Juice", price=3.0))

    # Show order
    order.show()