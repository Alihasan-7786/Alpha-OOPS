import csv


class Item:
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# Creating instances from CSV
Item.instantiate_from_csv()
print(Item.all)
# Checking integer values
print(Item.is_integer(7))
print(Item.is_integer(7.5))
print(Item.is_integer(7.0))