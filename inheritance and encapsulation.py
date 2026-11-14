class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.all.append(self)
    @property
    def name(self):
        print("You are trying to get name")
        return self.__name
    @name.setter
    def name(self, value):
        print("You are trying to set name")
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
    @property
    def price(self):
        return self.__price
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

item1 = Item("MyItem", 750, 6)

print(item1.name)
item1.name = "OtherItem"
print(item1.name)
try:
    item1.name = "OtherItem123"
except Exception as e:
    print("Exception:", e)
print(item1.price)
try:
    item1.price = -900
except AttributeError as e:
    print("AttributeError:", e)
item1.apply_increment(0.2)
print(item1.price)

item1.apply_discount()
print(item1.price)