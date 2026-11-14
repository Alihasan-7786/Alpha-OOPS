# Abstraction
class Item:
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __connect(self, smpt_server):
        pass
    def __prepare_body(self):
        return f"""
        Hello someone.
        We have {self.name} {self.quantity} times.
        Regards, Jim
        """
    def __send(self):
        pass
    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()
        print("email sent (simulation)")

item1 = Item("MyItem", 750, 6)
item1.send_email()
try:
    item1.__connect("")
except AttributeError as e:
    print("AttributeError:", e)

# Inheritance
class Item:
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.__price = price
        self.quantity = quantity
    @property
    def price(self):
        return self.__price
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
    def send_email(self):
        print(f"email about {self.name} sent (simulation)")

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

item1 = Phone("jscPhonev10", 1000, 5, 1)
item1.send_email()
item1.apply_increment(0.2)
print(item1.price)

# Polymorphism
print(len("Hello"))
print(len(["one", "two", "three"]))
print(len({"a": 1, "b": 2}))
