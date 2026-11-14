class Item:
    def __init__(self):
        print("I am created")
# Creating two objects
item1 = Item()
item2 = Item()

class Item:
    def __init__(self, name):
        print(f"An instance created: {name}")
        self.name = name
# Passing names while creating objects
item1 = Item("Phone")
item2 = Item("Laptop")
print(item1.name)
print(item2.name)

class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
# Creating items with their details
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10)
print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(item3.quantity)
print(item3.calculate_total_price())
# Adding an extra attribute to the laptop
item2.has_numpad = False
print(item2.has_numpad)

class Item:
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
# Passing price as a string
item1 = Item("Laptop", "1000", 3)
print(item1.calculate_total_price())
print(type(item1.price))

class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Checking the values before assigning them
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        # Assigning the values to the object
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = Item("Phone", 100, 1)
print("valid item created:", item1.name)
# Checking what happens when negative values are passed
try:
    Item("Laptop", -100, 3)
except AssertionError as e:
    print("AssertionError:", e)
try:
    Item("Laptop", 1000, -1)
except AssertionError as e:
    print("AssertionError:", e)

class Item:
    pay_rate = 0.8        # the pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

# Creating two different items
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)
print("--- class level __dict__ (without magic keys) ---")
print([k for k in Item.__dict__ if not k.startswith("__")])
print("--- instance level __dict__ ---")
print(item1.__dict__)


class ItemWrong:
    pay_rate = 0.8
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def apply_discount(self):
        self.price = self.price * ItemWrong.pay_rate
class Item:
    pay_rate = 0.8
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
# Applying the discount to a phone
item1 = Item("Phone", 100, 1)
item1.apply_discount()
print("phone after 20% discount:", item1.price)
print("--- laptop with its own 30% discount ---")
# Giving this laptop its own discount rate
wrong = ItemWrong("Laptop", 1000, 3)
wrong.pay_rate = 0.7
wrong.apply_discount()
print("using ItemWrong.pay_rate:", wrong.price)
right = Item("Laptop", 1000, 3)
right.pay_rate = 0.7
right.apply_discount()
print("using self.pay_rate:     ", right.price)

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

        # Keeping track of every object created
        Item.all.append(self)
# Creating five different items
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
print(len(Item.all))
# Printing the name of every item
for instance in Item.all:
    print(instance.name)

class Plain:
    all = []
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        Plain.all.append(self)

class Item:
    all = []
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# Creating objects from both classes
Plain("Phone", 100, 1)
Plain("Laptop", 1000, 3)
Item("Phone", 100, 1)
Item("Laptop", 1000, 3)
Item("Cable", 10, 5)
# Comparing how both lists are printed
print("without __repr__:", Plain.all)
print("with __repr__:   ", Item.all)