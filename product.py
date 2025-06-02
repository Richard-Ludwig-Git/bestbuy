
class Product:
    def __init__(self, name=None, price=0, quantity=0):
        self.Name = name
        if name is None:
            raise Exception("Name is not allowed to be empty")
        self.Price = price
        if price<0:
            raise Exception("Price could not be negative")
        self.Quantity = quantity
        if quantity < 0:
            raise Exception("Quantity could not be negative")
        self.Active = True


    def get_quantity(self):
        return self.Quantity


    def set_quantity(self, quantity):
        self.Quantity = quantity
        if quantity <= 0:
            self.Active = False


    def is_active(self):
        if self.Active:
            return True
        else:
            return False


    def deactivate(self):
        self.Active = False


    def activate(self):
        self.Active = True


    def show(self):
        print(f"{self.Name}, Price: {self.Price}, Quantity: {self.Quantity}")


    def buy(self, quantity):
        try:
            self.Quantity -= int(quantity)
            return self.Price * int(quantity)
        except ValueError:
            return "Sorry, wrong Value"